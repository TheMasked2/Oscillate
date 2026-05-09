import numpy as np

class Oscillator:
    def __init__(self, amplitude=1.0, sample_rate=44100):
        self.amplitude = amplitude
        self.sample_rate = sample_rate
    
    def generate_waveform(self, frequency, duration, waveform='sine'):
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        if waveform == 'sine':
            return self.amplitude * np.sin(2 * np.pi * frequency * t)
        elif waveform == 'square':
            return self.amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
        elif waveform == 'saw':
            return self.amplitude * (2 * (t * frequency - np.floor(1/2 + t * frequency)))
        elif waveform == 'triangle':
            return self.amplitude * (2 * np.abs(2 * (t * frequency - np.floor(1/2 + t * frequency))) - 1)
        else:
            raise ValueError("Unsupported waveform type")
        
    # waveform existing of multiple frequencies waveforms e.g. sin + square + saw
    def generate_complex_waveform(self, frequencies, duration, waveforms):
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        complex_waveform = np.zeros_like(t)
        for freq, wave in zip(frequencies, waveforms):
            complex_waveform += self.generate_waveform(freq, duration, wave)
        return complex_waveform / len(frequencies)  # Normalize the amplitude
