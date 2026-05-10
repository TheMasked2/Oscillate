class Track:
    def __init__(self, name, instrument='sine', volume=1.0, mute=False, solo=False):
        self.name = name
        self.instrument = instrument
        self.volume = volume
        self.mute = mute
        self.solo = solo
        self.clips = []

    def add_clip(self, clip):
        self.clips.append(clip)

    def remove_clip(self, clip):
        if clip in self.clips:
            self.clips.remove(clip)

    def is_enabled(self):
        return not self.mute

    def toggle_mute(self):
        self.mute = not self.mute

    def toggle_solo(self):
        self.solo = not self.solo

    def set_volume(self, value: float):
        self.volume = max(0.0, min(1.0, value))

    def get_note_events(self):
        events = []
        for clip in self.clips:
            events.extend(clip.get_absolute_note_events())
        return events