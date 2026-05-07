import numpy as np

class Track:
    def __init__(self, name, waveform, volume=1.0, mute=False, solo=False):
        self.name = name
        self.waveform = np.asarray(waveform, dtype=np.float32)
        self.volume = float(volume)
        self.mute = bool(mute)
        self.solo = bool(solo)

class Mixer:
    def __init__(self):
        self.tracks = []

    def add_track(self, track: Track):
        self.tracks.append(track)

    def mix(self, normalize=True):
        if not self.tracks:
            return np.zeros(0, dtype=np.float32)

        solo_tracks = [t for t in self.tracks if t.solo]
        tracks = solo_tracks if solo_tracks else self.tracks

        active = [t for t in tracks if not t.mute]
        if not active:
            return np.zeros(0, dtype=np.float32)

        max_len = max(len(t.waveform) for t in active)
        mixed = np.zeros(max_len, dtype=np.float32)

        for track in active:
            wave = track.waveform * track.volume
            if len(wave) < max_len:
                wave = np.pad(wave, (0, max_len - len(wave)), mode="constant")
            mixed += wave

        if normalize:
            peak = np.max(np.abs(mixed))
            if peak > 0:
                mixed = mixed / peak
        return mixed.astype(np.float32)