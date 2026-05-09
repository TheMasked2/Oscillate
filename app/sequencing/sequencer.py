from dataclasses import dataclass
from app.core.project import Project

@dataclass
class SequencedNote:
    track: object
    event: object

    @property
    def start_time(self):
        return self.event.start_time

    @property
    def end_time(self):
        return self.event.end_time

    @property
    def pitch(self):
        return self.event.pitch

    @property
    def velocity(self):
        return self.event.velocity

    @property
    def duration(self):
        return self.event.duration

class Sequencer:
    def __init__(self, project: Project):
        self.project = project
        self.settings = project.settings

    def sequence(self):
        all_notes = []
        solo_tracks = [track for track in self.project.tracks if track.solo]
        use_solo = len(solo_tracks) > 0

        for track in self.project.tracks:
            if use_solo and not track.solo:
                continue
            if not use_solo and track.mute:
                continue

            for event in track.get_note_events():
                all_notes.append(SequencedNote(track=track, event=event))

        all_notes.sort(key=lambda note: note.start_time)
        return all_notes