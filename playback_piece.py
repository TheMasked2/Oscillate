import numpy as np
import sounddevice as sd
import re

from load_notes import load_notes
from load_chords import load_chords

from playback_chord import return_chord_wave
from playback_melody import return_melody_wave


def generate_piece(melody: list | None = None, base_melody: list | None = None, chords: list | None = None,
                   duration: float = 4.0, amp: float = 0.2, sr: int = 44100, type: str = "sine"):
    """Merges a melody, optional base melody, and chord progression into a single waveform."""
    melody_wave = return_melody_wave(melody, duration, amp=amp, sr=sr, type=type) if melody else np.zeros(0, dtype=np.float32)
    base_wave = return_melody_wave(base_melody, duration, amp=amp, sr=sr, type=type) if base_melody else np.zeros(0, dtype=np.float32)
    chord_wave = return_chord_wave(chords, duration, amp=0.4, sr=sr, type=type) if chords else np.zeros(0, dtype=np.float32)

    max_len = max(len(melody_wave), len(base_wave), len(chord_wave))
    if max_len == 0:
        return np.zeros(0, dtype=np.float32)

    if len(melody_wave) < max_len:
        melody_wave = np.pad(melody_wave, (0, max_len - len(melody_wave)), mode="constant")
    if len(base_wave) < max_len:
        base_wave = np.pad(base_wave, (0, max_len - len(base_wave)), mode="constant")
    if len(chord_wave) < max_len:
        chord_wave = np.pad(chord_wave, (0, max_len - len(chord_wave)), mode="constant")

    piece = melody_wave + base_wave + chord_wave
    piece /= np.max(np.abs(piece)) if np.any(piece) else 1.0
    return piece.astype(np.float32)

def _play(wave, sr=44100, volume=0.4):
    sd.play(wave * volume, sr)
    sd.wait()

def main():
    # Mary had a little lamb in C major
    # melody = [
    #     ("E4", 0.5), ("D4", 0.5), ("C4", 0.5), ("D4", 0.5),
    #     ("E4", 0.5), ("E4", 0.5), ("E4", 1.0),
    #     ("D4", 0.5), ("D4", 0.5), ("D4", 1.0),
    #     ("E4", 0.5), ("G4", 0.5), ("G4", 1.0),
    #     ("E4", 0.5), ("D4", 0.5), ("C4", 0.5), ("D4", 0.5),
    #     ("E4", 0.5), ("E4", 0.5),  ("E4", 0.5), ("E4", 0.5),
    #     ("D4", 0.5), ("D4", 0.5), ("E4", 0.5), ("D4", 0.5), ("C4", 1.0)
    # ]

    # chords = [
    #     ("C3maj", 4.0), ("F3maj", 2.0), ("G3maj", 2.0), ("C3maj", 4.0), ("F3maj", 2.0), ("C3maj", 1.0)
    # ]

    # chopin nocturne 20 in C# minor
    # melody = [
    #     # 1st bar
    #     ("F#5", 2.0), 
    #     ("G#5", 0.15), ("F#5", 0.15), ("G#5", 0.15), ("F#5", 0.15), ("G#5", 0.12), ("F#5", 0.12),
    #     ("G#5", 0.12), ("F#5", 0.12), ("G#5", 0.12), ("F#5", 0.07), ("G#5", 0.07), ("F#5", 0.07), ("G#5", 0.07),
    #     ("F#5", 0.07), ("G#5", 0.07), ("F#5", 0.15), ("G#5", 0.15), ("F#5", 0.15), ("G#5", 0.15), 
        
        
        
    #     ("E5", 0.20), ("F#5", 0.25), ("G#5", 2.0),
    # ]

    melody = [
        # 1st bar 
        ("F#5", 2.0),
        ("G#5", 0.22), ("F#5", 0.2), ("G#5", 0.18), ("F#5", 0.16), ("G#5", 0.14),
        ("F#5", 0.12), ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1),
        ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1),
        ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1), 
        ("E5", 0.3), ("F#5", 0.45), ("G#5", 2.0), ("C#5", 1.0),

        # 3rd bar
        ("C#6", 2.0), ("B5", 0.2), ("C#6", 0.35), ("B5", 0.35), ("A5", 0.15), ("rest", 0.15), ("A5", 1.0),

        # # 4th bar

        
    ]

    sub_melody = [
        # 1st bar
        ("C#3", 0.9), ("G#3", 0.55), ("E4", 0.35), ("C#4", 0.2),
        ("C#3", 0.9), ("A3", 0.55), ("D#4", 0.35), ("C#4", 0.2),

        # 2nd bar
        ("C#3", 0.9), ("G#3", 0.55), ("E4", 0.35), ("C#4", 0.2),
        ("C#3", 0.9), ("G#3", 0.55), ("E4", 0.35), ("C#4", 0.2),

        # 3rd bar
        ("C#3", 0.9), ("G#3", 0.55), ("F4", 0.35), ("C#4", 0.2),
        ("C#3", 0.9), ("G#3", 0.55), ("F4", 0.35), ("C#4", 0.2),

        # #4th bar
        # ("E3", 0.9), ("A3", 0.55), ("F#4", 0.35), ("C#4", 0.2),
        # ("E3", 0.9), ("A3", 0.55), ("F#4", 0.35), ("C#4", 0.2),
    ]

    chords = []

    piece = generate_piece(melody, sub_melody, chords, duration=4.0)
    _play(piece, volume=0.2)

if __name__ == "__main__":
    main()