import json
from pathlib import Path

class MusicData:
    def __init__(self):
        data_dir = Path(__file__).resolve().parent.parent / 'data'
        
        with open(data_dir / 'notes.json') as f:
            self.notes = json.load(f)
        
        with open(data_dir / 'chords.json') as f:
            self.chords = json.load(f)

        with open(data_dir / 'note_offsets.json') as f:
            self.note_offsets = json.load(f)

    def get_notes(self, note_name):
        return self.notes[note_name]
    
    def get_frequency(self, note_name):
        return self.notes[note_name]['frequency']

    def get_chord_intervals(self, chord_name):
        return self.chords[chord_name]

    def get_note_offset(self, note_name):
        return self.note_offsets.get(note_name, 0)
    
    def _note_name_to_midi(self, note_name):
        # Convert note name to MIDI number (e.g., C4 -> 60)
        base_note = note_name[:-1]
        octave = int(note_name[-1])
        offset = self.get_note_offset(base_note)
        return 12 * (octave + 1) + offset
    
    def midi_to_frequency(self, midi_number):
        # Convert MIDI number to frequency
        return 440.0 * (2 ** ((midi_number - 69) / 12))