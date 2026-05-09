import numpy as np
from app.rendering.audio_renderer import AudioRenderer
from app.audio.envelope import Envelope
from app.sequencing.sequencer import Sequencer

class Mixer:
    def __init__(self, project):
        self.project = project
        self.sequencer = Sequencer(project)
        self.sample_rate = project.settings.sample_rate
        self.envelope = Envelope(sample_rate=self.sample_rate)

    def mix(self):
        sequenced_notes = self.sequencer.sequence()
        renderer = AudioRenderer(self.sample_rate, sequenced_notes)
        rendered_audio = renderer.render()
        rendered_audio = self._normalize(rendered_audio)
        return self.apply_fade(rendered_audio)

    def apply_fade(self, audio):
        return self.envelope.apply_fade(audio, fade_time=0.01)

    def _normalize(self, audio):
        if audio.size == 0:
            return audio
        peak = np.max(np.abs(audio))
        if peak > 1.0:
            return audio / peak
        return audio