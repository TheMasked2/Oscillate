import numpy as np

class Envelope:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def apply_adsr(self, audio_data: np.ndarray,
                   attack: float, decay: float,
                   sustain_level: float, release: float) -> np.ndarray:
        n = len(audio_data)
        if n == 0:
            return audio_data

        attack_samples = int(round(attack * self.sample_rate))
        decay_samples = int(round(decay * self.sample_rate))
        release_samples = int(round(release * self.sample_rate))

        sustain_samples = n - attack_samples - decay_samples - release_samples
        if sustain_samples < 0:
            total = attack_samples + decay_samples + release_samples
            if total == 0:
                return audio_data
            scale = n / total
            attack_samples = int(round(attack_samples * scale))
            decay_samples = int(round(decay_samples * scale))
            release_samples = n - attack_samples - decay_samples
            sustain_samples = 0

        attack_env = np.linspace(0.0, 1.0, attack_samples, endpoint=False, dtype=np.float32)
        decay_env = np.linspace(1.0, sustain_level, decay_samples, endpoint=False, dtype=np.float32)
        sustain_env = np.full(sustain_samples, sustain_level, dtype=np.float32)
        release_env = np.linspace(sustain_level, 0.0, release_samples, endpoint=True, dtype=np.float32)

        envelope = np.concatenate([attack_env, decay_env, sustain_env, release_env])
        if len(envelope) < n:
            envelope = np.pad(envelope, (0, n - len(envelope)), mode="constant", constant_values=sustain_level)
        elif len(envelope) > n:
            envelope = envelope[:n]

        return audio_data * envelope
    
    def apply_fade(self, audio_data: np.ndarray, fade_time: float = 0.01) -> np.ndarray:
        n = len(audio_data)
        if n == 0 or fade_time <= 0.0:
            return audio_data

        fade_samples = min(int(round(fade_time * self.sample_rate)), n // 2)
        if fade_samples <= 0:
            return audio_data

        fade_in = np.linspace(0.0, 1.0, fade_samples, dtype=np.float32)
        fade_out = np.linspace(1.0, 0.0, fade_samples, dtype=np.float32)

        audio_data[:fade_samples] *= fade_in
        audio_data[-fade_samples:] *= fade_out
        return audio_data