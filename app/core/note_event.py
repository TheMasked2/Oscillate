class NoteEvent:
    def __init__(self, pitch, velocity, start_time, duration):
        self.pitch = pitch
        self.velocity = velocity
        self.start_time = start_time
        self.duration = duration

    @property
    def end_time(self):
        return self.start_time + self.duration