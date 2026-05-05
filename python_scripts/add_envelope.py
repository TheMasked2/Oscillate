import numpy as np

def apply_envelope(waveform: np.ndarray, sample_rate: int, fade_ms: float = 50, add_tail: bool = True) -> np.ndarray:
    fade_samples = int(sample_rate * (fade_ms / 1000))
    if len(waveform) < 2 * fade_samples:
        return waveform

    ramp = np.hanning(2 * fade_samples)
    attack = ramp[:fade_samples]
    release = ramp[fade_samples:]
    waveform[:fade_samples] *= attack
    waveform[-fade_samples:] *= release

    if add_tail:
        tail = np.zeros(int(sample_rate * 0.15), dtype=np.float32)
        return np.concatenate([waveform, tail])
    return waveform