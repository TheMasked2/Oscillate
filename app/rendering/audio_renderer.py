import numpy as np
from data.data_loader import MusicData
from app.audio.oscillator import Oscillator

WAVEFORM_MAP = {
    'sine': 'sine',
    'square': 'square',
    'saw': 'saw',
    'triangle': 'triangle',
    'piano': 'triangle',
    'bass': 'square',
    'default': 'sine',
}

class AudioRenderer:
    def __init__(self, sample_rate, sequenced_notes):
        self.sample_rate = sample_rate
        self.data_loader = MusicData()
        self.oscillator = Oscillator(sample_rate=sample_rate)
        self.sequenced_notes = sequenced_notes or []

    def _waveform_for_track(self, track):
        return WAVEFORM_MAP.get(track.instrument, WAVEFORM_MAP['default'])

    def _frequency_for_pitch(self, pitch):
        if pitch == 'rest':
            return 0.0
        return self.data_loader.get_frequency(pitch)

    def _write_note_to_buffer(self, buffer, start_sample, note_audio, amplitude):
        if start_sample >= len(buffer):
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
            track_id = sequenced_note.track.name
            track_buffer = track_buffers.setdefault(
                track_id, np.zeros(total_samples, dtype=np.float32)
            )

            waveform_name = self._waveform_for_track(sequenced_note.track)
            frequency = self._frequency_for_pitch(sequenced_note.pitch)

            if frequency <= 0.0:
                continue

            note_audio = self.oscillator.generate_waveform(
                frequency,
                sequenced_note.duration,
                waveform_name
            )

            amplitude = (sequenced_note.velocity / 127.0) * sequenced_note.track.volume
            start_sample = int(np.round(sequenced_note.start_time * self.sample_rate))

            self._write_note_to_buffer(track_buffer, start_sample, note_audio, amplitude)

        return track_buffers

    def render(self, mix_tracks=True):
        track_buffers = self.render_track_buffers()
        if not track_buffers:
            return np.zeros(0, dtype=np.float32)

        if not mix_tracks:
            return track_buffers

        mixed = np.zeros(
            max(len(buf) for buf in track_buffers.values()), dtype=np.float32
        )
        for buffer in track_buffers.values():
            mixed[: len(buffer)] += buffer
        return mixed