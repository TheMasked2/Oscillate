from core.data_loader import MusicData
from core.oscillator import Oscillator
from core.player import AudioPlayer
from features.melody_builder import MelodyBuilder
from features.chord_builder import ChordBuilder
from features.mixer import Mixer, Track

music_data = MusicData()
oscillator = Oscillator()
audio_player = AudioPlayer()
melody_builder = MelodyBuilder(music_data, oscillator)
chord_builder = ChordBuilder(music_data, oscillator)
mixer = Mixer()

# play a simple melody
melody = [
    # 1st bar 
    ("F#5", 2.0),
    ("G#5", 0.22), ("F#5", 0.2), ("G#5", 0.18), ("F#5", 0.16), ("G#5", 0.14),
    ("F#5", 0.12), ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1),
    ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1),
    ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1), 
    ("E5", 0.3), ("F#5", 0.45), ("G#5", 2.0), ("C#5", 1.0),

    # 3rd bar
    ("C#6", 2.0), ("B5", 0.2), ("C#6", 0.35), ("B5", 0.35), ("A5", 0.15), ("rest", 0.15), ("A5", 1.0)
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



# play the melody
mixer = Mixer()
mixer.add_track(Track("melody", melody_builder.build_melody(melody), volume=0.7))
mixer.add_track(Track("sub", melody_builder.build_melody(sub_melody), volume=0.5))
# mixer.add_track(Track("chords", chord_builder.build_chord("C#3", "major", duration=4.0), volume=0.4))

final = mixer.mix()
audio_player.play(final, volume=0.2)