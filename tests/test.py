from app.audio.envelope import Envelope
from app.audio.data_loader import MusicData
from app.audio.oscillator import Oscillator
from app.engine.chord_builder import ChordBuilder
from app.engine.melody_builder import MelodyBuilder
from app.audio.mixer import Mixer, Track
from app.playback.player import AudioPlayer

music_data = MusicData()
oscillator = Oscillator()
envelope = Envelope()
chord_builder = ChordBuilder(music_data, oscillator, adsr=envelope)
melody_builder = MelodyBuilder(music_data, oscillator, adsr=envelope)
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