import numpy as np

class MelodyBuilder:
    def __init__(self, music_data, oscillator, adsr=None):
        self.music_data = music_data
        self.oscillator = oscillator
        self.adsr = adsr

    def build_note(self, note, duration, amplitude=1.0, waveform="sine", adsr=None):
        if note == "rest":
            return np.zeros(int(self.oscillator.sample_rate * duration), dtype=np.float32)

        freq = self.music_data.get_notes(note)
        wave = self.oscillator.generate_waveform(freq, duration, waveform) * amplitude

        params = adsr or self.adsr
        if params:
            wave = self.adsr.apply_adsr(wave, **params)
        return wave.astype(np.float32)

    def build_melody(self, sequence, amplitude=1.0, waveform="sine", adsr=None):
        waves = [
            self.build_note(note, duration, amplitude=amplitude, waveform=waveform, adsr=adsr)
            for note, duration in sequence
        ]
        if not waves:
            return np.zeros(0, dtype=np.float32)
        return np.concatenate(waves).astype(np.float32)