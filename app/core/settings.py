class Settings:
    def __init__(self, sample_rate=44100, tempo=120, time_signature=(4, 4), key_signature='C'):
        self.sample_rate = sample_rate
        self.tempo = tempo
        self.time_signature = time_signature
        self.key_signature = key_signature