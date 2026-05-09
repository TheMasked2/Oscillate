import numpy as np
from data.data_loader import MusicData
from app.audio.oscillator import Oscillator
from app.audio.envelope import Envelope
from app.instruments.test_instrument import get_instrument_preset

class AudioRenderer:
    def __init__(self, sample_rate, sequenced_notes):
        self.sample_rate = sample_rate
        self.data_loader = MusicData()
        self.oscillator = Oscillator(sample_rate=sample_rate)
        self.envelope = Envelope(sample_rate=sample_rate)
        self.sequenced_notes = sequenced_notes or []

    def _frequency_for_pitch(self, pitch):
        if pitch == "rest":
            return 0.0
        return self.data_loader.get_frequency(pitch)

    def _render_note_audio(self, note, preset):
        frequency = self._frequency_for_pitch(note.pitch)
        if frequency <= 0.0:
            return np.zeros(0, dtype=np.float32)

        note_audio = self.oscillator.generate_waveform(
            frequency,
            note.duration,
            preset.waveform,
        )

        adsr = preset.adsr
        return self.envelope.apply_adsr(
            note_audio,
            adsr.get("attack", 0.01),
            adsr.get("decay", 0.05),
            adsr.get("sustain_level", 0.8),
            adsr.get("release", 0.1),
        )

    def _write_note_to_buffer(self, buffer, start_sample, note_audio, amplitude):
        if start_sample >= len(buffer) or note_audio.size == 0:
            return
        end_sample = min(len(buffer), start_sample + len(note_audio))
        buffer[start_sample:end_sample] += note_audio[: end_sample - start_sample] * amplitude

    def render_track_buffers(self):
        if not self.sequenced_notes:
            return {}

        total_duration = max(note.end_time for note in self.sequenced_notes)
        total_samples = int(np.ceil(total_duration * self.sample_rate))
        track_buffers = {}

        for sequenced_note in self.sequenced_notes:
            preset = get_instrument_preset(sequenced_note.track.instrument)
            track_buffer = track_buffers.setdefault(
                sequenced_note.track.name,
                np.zeros(total_samples, dtype=np.float32),
            )

            note_audio = self._render_note_audio(sequenced_note, preset)
            if note_audio.size == 0:
                continue

            amplitude = (sequenced_note.velocity / 127.0) * sequenced_note.track.volume
            start_sample = int(round(sequenced_note.start_time * self.sample_rate))
            self._write_note_to_buffer(track_buffer, start_sample, note_audio, amplitude)

        return track_buffers

    def render(self):
        track_buffers = self.render_track_buffers()
        if not track_buffers:
            return np.zeros(0, dtype=np.float32)

        mixed = np.zeros(
            max(len(buffer) for buffer in track_buffers.values()),
            dtype=np.float32,
        )
        for buffer in track_buffers.values():
            mixed[: len(buffer)] += buffer

        return mixed