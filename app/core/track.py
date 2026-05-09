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

    def get_note_events(self):
        events = []
        for clip in self.clips:
            events.extend(clip.get_absolute_note_events())
        return events