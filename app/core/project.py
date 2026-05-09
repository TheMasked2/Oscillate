from app.core.settings import Settings

class Project:
    def __init__(self, name, settings=None):
        self.name = name
        self.settings = settings or Settings()
        self.tracks = []

    def add_track(self, track):
        if track not in self.tracks:
            self.tracks.append(track)

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)

    def get_all_clips(self):
        clips = []
        for track in self.tracks:
            clips.extend(track.clips)
        return clips

    def add_clip_to_track(self, clip, track):
        if track in self.tracks:
            track.add_clip(clip)

    def remove_clip_from_track(self, clip, track):
        if track in self.tracks:
            track.remove_clip(clip)

    def get_all_note_events(self):
        events = []
        for track in self.tracks:
            events.extend(track.get_note_events())
        return events

    def get_project_duration(self):
        max_time = 0
        for clip in self.get_all_clips():
            if clip.end_time > max_time:
                max_time = clip.end_time
        return max_time