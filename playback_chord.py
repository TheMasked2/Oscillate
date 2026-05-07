import numpy as np
import sounddevice as sd
import re

from load_notes import load_notes
from load_chords import load_chords
from add_envelope import apply_envelope

notes_dict = load_notes()
chords_dict = load_chords()

NOTES_ORDER = ["C", "C#", "D", "D#", "E", "F",
               "F#", "G", "G#", "A", "A#", "B"]

def parse_chord_symbol(symbol: str):
    """
    Parses a chord symbol (e.g., "C4maj", "A3min7") and returns the root note and chord type
    """

    match = re.match(r"([A-G]#?)(\d)(.*)", symbol)
    if not match:
        raise ValueError("Invalid chord format")

    root_note = match.group(1) + match.group(2)
    chord_type = match.group(3)

    if chord_type == "maj":
        chord_type = "major"
    elif chord_type == "min":
        chord_type = "minor"
    elif chord_type == "min7":
        chord_type = "minor7"
    elif chord_type == "maj7":
        chord_type = "major7"
    elif chord_type == "dom7":
        chord_type = "dominant7"
    elif chord_type == "pow":
        chord_type = "power"

    return root_note, chord_type

def note_to_midi(note):
    name = note[:-1]
    octave = int(note[-1])
    return (octave + 1) * 12 + NOTES_ORDER.index(name)

def midi_to_note(midi):
    name = NOTES_ORDER[midi % 12]
    octave = midi // 12 - 1
    return f"{name}{octave}"

def build_chord(root, chord_type, chords_dict):
    root_midi = note_to_midi(root)
    intervals = chords_dict[chord_type]

    return [midi_to_note(root_midi + i) for i in intervals]

def chord_to_freqs(notes, notes_dict):
    return [notes_dict[n] for n in notes]

def generate_wave(freqs, amp, duration, sr, type, add_tail=True):
    """Generates a waveform for a chord based on the given frequencies, amplitude, duration, sample rate, and wave type."""	
    t = np.linspace(0, duration, int(sr * duration), False)
    wave = np.zeros_like(t)
    for f in freqs:
        if type == "sine":
            wave += np.sin(2 * np.pi * f * t)
        elif type == "square":
            wave += np.sign(np.sin(2 * np.pi * f * t))
        elif type == "sawtooth":
            wave += 2 * (t * f - np.floor(0.5 + t * f))
    wave /= len(freqs)
    wave = apply_envelope(wave, sr, add_tail=add_tail) # Apply an envelope to the wave to prevent clicks
    wave /= np.max(np.abs(wave))
    wave *= amp
    return wave.astype(np.float32)

def return_chord_wave(chords, duration, amp=0.8, sr=44100, type="sine"):
    waves = []
    for chord, duration in chords:
        root, chord_type = parse_chord_symbol(chord)
        chord_notes = build_chord(root, chord_type, chords_dict)
        freqs = chord_to_freqs(chord_notes, notes_dict)
        waves.append(generate_wave(freqs, amp, duration, sr, type, add_tail=False))
    progression = np.concatenate(waves)
    progression = apply_envelope(progression, sr)
    return progression

def play_chords(chords, amp=0.8, sr=44100, type="sine"):
    """Plays a chord progression defined as a list of chord/duration tuples."""	
    waves = []
    for chord, duration in chords:
        root, chord_type = parse_chord_symbol(chord)
        chord_notes = build_chord(root, chord_type, chords_dict)
        freqs = chord_to_freqs(chord_notes, notes_dict)
        waves.append(generate_wave(freqs, amp, duration, sr, type, add_tail=False))

    progression = np.concatenate(waves)
    progression = apply_envelope(progression, sr)
    _play(progression, sr)

def _play(wave, sr=44100, volume=0.4):
    sd.play(wave * volume, sr)
    sd.wait()

def main():
    # simple chord progression
    chord_progression = [
        ("C3maj", 2.0),
        ("F3maj", 1.5),
        ("G3maj", 1.0),
        ("C3maj", 2.0),
    ]

    play_chords(chord_progression, type="sine")

if __name__ == "__main__":
    main()