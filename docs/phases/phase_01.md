## Goal

Turn the current synth prototype into a clean foundation.

## Main Focus

* note rendering
* timing consistency
* stereo support
* effects foundation
* clean architecture

## Features

* ADSR cleanup
* detune
* stereo rendering
* lowpass filters
* simple reverb
* effect chains
* better mixer

## Learning Goals

By the end of this phase you should understand:

* digital audio basics
* envelopes
* oscillators
* waveform layering
* stereo audio
* simple DSP
* audio mixing

## Deliverable

A synth engine capable of rendering decent-sounding ambient/chiptune music.

---

# Recommended Files

```text
app/audio/
    oscillator.py
    envelope.py
    filters.py
    effects.py
    mixer.py
```

---

# Important Concepts To Research

## Detune

Example:

```python
wave1 = osc(freq * 0.995)
wave2 = osc(freq)
wave3 = osc(freq * 1.005)
```

Creates:

* width
* warmth
* movement

---

## Stereo Rendering

Example:

```python
left = wave
right = np.roll(wave, 100)
```

Creates:

* space
* immersion

---

## Lowpass Filters

Research:

* one-pole filters
* butterworth filters
* cutoff frequency

---

## Reverb

Research:

* delay lines
* feedback
* convolution reverb (later)

---