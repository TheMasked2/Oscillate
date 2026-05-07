import numpy as np

class ChordBuilder:
    def __init__(self, music_data, oscillator):
        self.music_data = music_data
        self.oscillator = oscillator

    def build_chord(self, root_note, chord_type, duration=2.0,
                    amplitude=0.4, waveform="sine"):
        root_freq = self.music_data.get_notes(root_note)
        intervals = self.music_data.get_chord_intervals(chord_type)

        waves = [
            self.oscillator.generate_waveform(root_freq * 2**(interval / 12),
                                              duration, waveform)
            for interval in intervals
        ]
        chord_wave = sum(waves) / len(waves)
        return chord_wave.astype(np.float32)