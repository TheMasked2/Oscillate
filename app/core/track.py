import numpy as np

class Track:
    def __init__(self, name, waveform, volume=1.0, mute=False, solo=False):
        self.name = name
        self.waveform = np.asarray(waveform, dtype=np.float32)
        self.volume = float(volume)
        self.mute = bool(mute)
        self.solo = bool(solo)