import json
from pathlib import Path

class MusicData:
    def __init__(self):
        data_dir = Path(__file__).resolve().parent.parent / 'data'
        
        with open(data_dir / 'notes.json') as f:
            self.notes = json.load(f)
        
        with open(data_dir / 'chords.json') as f:
            self.chords = json.load(f)

    def get_notes(self, note_name):
        return self.notes[note_name]

    def get_chord_intervals(self, chord_name):
        return self.chords[chord_name]