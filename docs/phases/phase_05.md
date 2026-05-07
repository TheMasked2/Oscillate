## Goal

Turn the synth into an extensible sound engine.

---

# Features

## Instruments

* pads
* leads
* basses
* strings
* piano-ish plucks
* chiptune synths

## Effects

* reverb
* delay
* chorus
* detune
* distortion
* lowpass/highpass
* stereo widening

---

# Recommended Architecture

```python
Track
    -> Instrument
    -> Effect Chain
    -> Mixer
```

---

# Learning Goals

By the end of this phase you should understand:

* modular audio processing
* effect pipelines
* synthesis layering
* sound design fundamentals

---

# Deliverable

A modular synth/effects workflow.

---

# Important Concepts To Research

## Chorus

Research:

* delayed detuned copies
* modulation delay

---

## Delay

Example:

```python
wave += np.roll(wave, delay_samples) * feedback
```

---

## Saturation

Example:

```python
wave = np.tanh(wave * drive)
```

---
