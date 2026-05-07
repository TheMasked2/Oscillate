import os
import json

def load_chords(filename="chords.json"):
    # This gets the directory where load_notes.py actually lives
    script_dir = os.path.dirname(__file__) 
    
    # This joins that directory with your filename
    filepath = os.path.join(script_dir, filename)
    
    with open(filepath, "r") as f:
        return json.load(f)