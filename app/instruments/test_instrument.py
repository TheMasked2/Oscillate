from dataclasses import dataclass

@dataclass(frozen=True)
class InstrumentPreset:
    name: str
    waveform: str
    adsr: dict

DEFAULT_ADSR = {
    "attack": 0.01,
    "decay": 0.05,
    "sustain_level": 0.8,
    "release": 0.1,
}

INSTRUMENT_PRESETS = {
    "sine": InstrumentPreset(
        name="sine",
        waveform="sine",
        adsr=DEFAULT_ADSR,
    ),
    "triangle": InstrumentPreset(
        name="triangle",
        waveform="triangle",
        adsr={
            "attack": 0.01,
            "decay": 0.08,
            "sustain_level": 0.7,
            "release": 0.15,
        },
    ),
    "piano": InstrumentPreset(
        name="piano",
        waveform="triangle",
        adsr={
            "attack": 0.005,
            "decay": 0.1,
            "sustain_level": 0.6,
            "release": 0.2,
        },
    ),
    "bass": InstrumentPreset(
        name="bass",
        waveform="square",
        adsr={
            "attack": 0.01,
            "decay": 0.1,
            "sustain_level": 0.85,
            "release": 0.12,
        },
    ),
}

def get_instrument_preset(name: str) -> InstrumentPreset:
    return INSTRUMENT_PRESETS.get(name, INSTRUMENT_PRESETS["sine"])