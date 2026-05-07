from core.envelope import Envelope
from core.data_loader import MusicData
from core.oscillator import Oscillator
from features.chord_builder import ChordBuilder
from features.melody_builder import MelodyBuilder
from features.mixer import Mixer, Track
from core.player import AudioPlayer

music_data = MusicData()
oscillator = Oscillator()
envelope = Envelope()
chord_builder = ChordBuilder(music_data, oscillator, adsr=envelope)
melody_builder = MelodyBuilder(music_data, oscillator, adsr=envelope)
mixer = Mixer()
player = AudioPlayer()

# play a simple melody
# melody = [
#     # 1st bar 
#     ("F#5", 2.0),
#     ("G#5", 0.22), ("F#5", 0.2), ("G#5", 0.18), ("F#5", 0.16), ("G#5", 0.14),
#     ("F#5", 0.12), ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1),
#     ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1),
#     ("G#5", 0.1), ("F#5", 0.1), ("G#5", 0.1), ("F#5", 0.1), 
#     ("E5", 0.3), ("F#5", 0.45), ("G#5", 2.0), ("C#5", 1.0),

#     # 3rd bar
#     ("C#6", 2.0), ("B5", 0.2), ("C#6", 0.35), ("B5", 0.35), ("A5", 0.15), ("rest", 0.15), ("A5", 1.0)
# ]

# sub_melody = [
#         # 1st bar
#         ("C#3", 0.9), ("G#3", 0.55), ("E4", 0.35), ("C#4", 0.2),
#         ("C#3", 0.9), ("A3", 0.55), ("D#4", 0.35), ("C#4", 0.2),

#         # 2nd bar
#         ("C#3", 0.9), ("G#3", 0.55), ("E4", 0.35), ("C#4", 0.2),
#         ("C#3", 0.9), ("G#3", 0.55), ("E4", 0.35), ("C#4", 0.2),

#         # 3rd bar
#         ("C#3", 0.9), ("G#3", 0.55), ("F4", 0.35), ("C#4", 0.2),
#         ("C#3", 0.9), ("G#3", 0.55), ("F4", 0.35), ("C#4", 0.2),

#         # #4th bar
#         # ("E3", 0.9), ("A3", 0.55), ("F#4", 0.35), ("C#4", 0.2),
#         # ("E3", 0.9), ("A3", 0.55), ("F#4", 0.35), ("C#4", 0.2),
#     ]

from core.envelope import Envelope
from core.data_loader import MusicData
from core.oscillator import Oscillator
from features.chord_builder import ChordBuilder
from features.mixer import Mixer, Track
from core.player import AudioPlayer

music_data = MusicData()
oscillator = Oscillator()
envelope = Envelope()
chord_builder = ChordBuilder(music_data, oscillator, adsr=envelope)
mixer = Mixer()
player = AudioPlayer()

melody = [
    ("A4", 0.5),
    ("C5", 0.5),
    ("E5", 1.0),

    ("rest", 0.5),
    ("G5", 0.5),
    ("E5", 1.0),

    ("D5", 0.5),
    ("C5", 0.5),
    ("E5", 1.0),

    ("rest", 0.5),
    ("A5", 0.5),
    ("G5", 1.0),

    ("E5", 0.5),
    ("C5", 0.5),
    ("D5", 1.0),

    ("rest", 0.5),
    ("E5", 0.5),
    ("G5", 1.0),

    ("A5", 0.5),
    ("G5", 0.5),
    ("E5", 1.0),

    ("rest", 0.5),
    ("C5", 0.5),
    ("A4", 1.0),
]

bassline = [
    ("A2", 2.0),
    ("F2", 2.0),
    ("C3", 2.0),
    ("G2", 2.0),

    ("F2", 2.0),
    ("C3", 2.0),
    ("G2", 2.0),
    ("A2", 2.0),
]

melody_wave = melody_builder.build_melody(
    melody,
    amplitude=0.55,
    waveform="triangle",
    adsr={
        "attack": 0.01,
        "decay": 0.08,
        "sustain_level": 0.7,
        "release": 0.15,
    },
)

bass_wave = melody_builder.build_melody(
    bassline,
    amplitude=0.3,
    waveform="sine",
    adsr={
        "attack": 0.01,
        "decay": 0.05,
        "sustain_level": 0.85,
        "release": 0.1,
    },
)

mixer.add_track(Track("lead", melody_wave, volume=1.0))
mixer.add_track(Track("bass", bass_wave, volume=0.9))

final_wave = mixer.mix(normalize=True)
player.play(final_wave, volume=0.2)