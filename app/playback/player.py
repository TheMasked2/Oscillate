import time
import sounddevice as sd

from app.audio.mixer import Mixer

class Player:
    def __init__(self, mixer: Mixer):
        self.mixer = mixer
        self.original_buffer = None
        self.audio_buffer = None
        self.playback_start = None
        self.duration = 0.0
        self.playback_offset = 0.0
        self.pause_offset = 0.0
        self.is_paused = False

    def play(self, wait=False, start_sample=0):
        if self.original_buffer is None or start_sample == 0:
            self.original_buffer = self.mixer.mix()

        self.audio_buffer = self.original_buffer[start_sample:]
        if self.audio_buffer.size == 0:
            return

        self.playback_offset = start_sample / self.mixer.sample_rate
        self.duration = len(self.original_buffer) / self.mixer.sample_rate
        self.playback_start = time.perf_counter()
        self.is_paused = False
        sd.play(self.audio_buffer, samplerate=self.mixer.sample_rate)

        if wait:
            sd.wait()
            self.playback_start = None

    def pause(self):
        if not self.is_playing():
            return
        elapsed = time.perf_counter() - self.playback_start
        self.pause_offset = self.playback_offset + elapsed
        sd.stop()
        self.playback_start = None
        self.is_paused = True

    def resume(self):
        if not self.is_paused or self.original_buffer is None:
            return
        start_sample = int(round(self.pause_offset * self.mixer.sample_rate))
        self.play(start_sample=start_sample)

    def stop(self):
        sd.stop()
        self.playback_start = None
        self.is_paused = False
        self.pause_offset = 0.0
        self.playback_offset = 0.0
        self.original_buffer = None
        self.audio_buffer = None

    def is_playing(self):
        return self.playback_start is not None
    
    @property
    def current_position(self):
        if self.playback_start is None:
            return self.pause_offset
        elapsed = time.perf_counter() - self.playback_start
        return self.playback_offset + elapsed