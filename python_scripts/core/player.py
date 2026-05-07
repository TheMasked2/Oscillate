import sounddevice as sd

class AudioPlayer:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def play(self, audio_data, volume=1.0):
        sd.play(audio_data * volume, self.sample_rate)
        sd.wait()
