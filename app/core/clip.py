from app.core.note_event import NoteEvent

class Clip:
    def __init__(self, name, start_time, duration):
        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.note_events = []  # relative to clip.start_time

    def add_note_event(self, note_event):
        self.note_events.append(note_event)

    def remove_note_event(self, note_event):
        if note_event in self.note_events:
            self.note_events.remove(note_event)

    def get_absolute_note_events(self):
        return [
            NoteEvent(
                pitch=event.pitch,
                velocity=event.velocity,
                start_time=self.start_time + event.start_time,
                duration=event.duration
            )
            for event in self.note_events
        ]
    
    def get_note_events(self):
        return self.note_events

    @property
    def end_time(self):
        return self.start_time + self.duration