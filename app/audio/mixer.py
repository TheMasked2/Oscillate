from app.rendering.audio_renderer import AudioRenderer
from app.audio.envelope import Envelope
from app.sequencing.sequencer import Sequencer

class Mixer:
    def __init__(self, project):
        self.project = project
        self.sequencer = Sequencer(project)
        self.envelope = Envelope()
        self.sample_rate = project.settings.sample_rate

    def mix(self):
        sequenced_notes = self.sequencer.sequence()
        renderer = AudioRenderer(self.sample_rate, sequenced_notes)
        rendered_audio = renderer.render()
        return self.apply_envelope(rendered_audio)

    def apply_envelope(self, audio):
        return self.envelope.apply(audio)