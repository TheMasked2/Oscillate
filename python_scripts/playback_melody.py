import numpy as np
import sounddevice as sd

from load_notes import load_notes, get_frequency
from add_envelope import apply_envelope

notes = load_notes()  # Load the notes and their frequencies from notes.json

def generate_melody(freqs, duration, amp, sr, type, add_tail=True):
    if duration <= 0:
        return np.zeros(0, dtype=np.float32)

    t = np.linspace(0, duration, int(sr * duration), False)
    if not freqs:
        wave = np.zeros_like(t)
    else:
        wave = np.zeros_like(t)
        for f in freqs:
            if type == "sine":
                wave += np.sin(2 * np.pi * f * t)
            elif type == "square":
                wave += np.sign(np.sin(2 * np.pi * f * t))
            elif type == "sawtooth":
                wave += 2 * (t * f - np.floor(0.5 + t * f))
        wave /= len(freqs)

    wave = apply_envelope(wave, sr, add_tail=add_tail)

    max_val = np.max(np.abs(wave)) if wave.size else 0
    if max_val > 0:
        wave /= max_val

    wave *= amp
    return wave.astype(np.float32)

def return_melody_wave(melody, duration, amp=0.8, sr=44100, type="sine"):
    waves = []
    for note, duration in melody:
        if not note or str(note).lower() == "rest":
            waves.append(np.zeros(int(sr * duration), dtype=np.float32))
        else:
            waves.append(generate_melody([get_frequency(note, notes)], duration, amp, sr, type, False))

    if not waves:
        return np.zeros(0, dtype=np.float32)

    melody_wave = np.concatenate(waves)
    melody_wave = apply_envelope(melody_wave, sr)
    return melody_wave
    
def play_melody(melody, amp=0.8):
    """Plays a simple melody defined as a list of note/duration tuples."""
    waves = []
    for note, duration in melody:
        wave = generate_melody([get_frequency(note, notes)], duration, amp, 44100, "sine", False)
        waves.append(wave)
    melody = np.concatenate(waves)
    melody = apply_envelope(melody, 44100)
    play_note(melody)

def play_note(melody, sr=44100, volume=0.6):
    sd.play(melody * volume, sr)
    sd.wait()

def main():
    simple_melody = [
        ("C4", 0.5),
        ("D4", 0.5),
        ("E4", 0.5),
        ("F4", 0.5),
        ("G4", 0.5),
        ("A4", 0.5),
        ("B4", 0.5),
        ("C5", 1.0)
    ]

    play_melody(simple_melody)

if __name__ == "__main__":
    main()