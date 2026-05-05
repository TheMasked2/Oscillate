import os
import json

def load_notes(filename="notes.json"):
    # This gets the directory where load_notes.py actually lives
    script_dir = os.path.dirname(__file__) 
    
    # This joins that directory with your filename
    filepath = os.path.join(script_dir, filename)
    
    with open(filepath, "r") as f:
        return json.load(f)

def get_frequency(note: str, notes_dict: dict) -> float:
    """
    Lookup frequency from note string (e.g., 'C#4', 'A4')
    """
    note = note.strip().upper()

    if note not in notes_dict:
        raise ValueError(f"Note '{note}' not found in notes.json")

    return notes_dict[note]