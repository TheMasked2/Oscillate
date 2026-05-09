import sounddevice as sd

from app.audio.mixer import Mixer

class Player:
    def __init__(self, mixer: Mixer):
        self.mixer = mixer

    def play(self):
        audio_buffer = self.mixer.mix()
        if audio_buffer.size > 0:
            sd.play(audio_buffer, samplerate=self.mixer.sample_rate)
            sd.wait()