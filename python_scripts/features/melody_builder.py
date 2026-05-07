import numpy as np

class MelodyBuilder:
    def __init__(self, music_data, oscillator):
        self.music_data = music_data
        self.oscillator = oscillator

    def build_note(self, note, duration, amplitude=1.0, waveform="sine"):
        if note == "rest":
            return np.zeros(int(self.oscillator.sample_rate * duration), dtype=np.float32)
        freq = self.music_data.get_notes(note)
        return self.oscillator.generate_waveform(freq, duration, waveform) * amplitude

    def build_melody(self, sequence, amplitude=0.8, waveform="sine"):
        waves = [
            self.build_note(note, duration, amplitude, waveform)
            for note, duration in sequence
        ]
        if not waves:
            return np.zeros(0, dtype=np.float32)
        return np.concatenate(waves).astype(np.float32)