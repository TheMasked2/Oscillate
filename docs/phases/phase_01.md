# Phase 1 — Stabilize Core Audio Engine

# Phase 1 Execution Plan

## Goal

Turn the current synth prototype into a stable and reusable audio foundation.

This phase is NOT about perfection.

It is about:
- consistency
- structure
- reusable audio generation
- understanding synthesis fundamentals

---

# Recommended Development Order

## Step 1 — Clean Oscillator Interface

### Goal

Create a reusable oscillator API.

---

### Example

```python
oscillator.generate(
    frequency=440,
    duration=1.0,
    waveform="sine"
)
```

---

### Success Criteria

You can:
- generate sine waves
- generate square waves
- generate saw waves
- generate triangle waves
- switch waveforms cleanly

---

### Files

```text
app/audio/oscillator.py
```

---

## Step 2 — Stabilize ADSR Envelopes

### Goal

Apply ADSR consistently to all generated notes.

---

### Important Concept

Release should exist INSIDE total note duration.

NOT:

```text
wave + extra release tail
```

---

### Success Criteria

You can:
- hear attack clearly
- hear release clearly
- avoid clicks/pops
- apply ADSR to every waveform

---

### Files

```text
app/audio/envelope.py
```

---

## Step 3 — Add Detune

### Goal

Layer multiple slightly detuned oscillators.

---

### Example

```python
wave1 = osc(freq * 0.995)
wave2 = osc(freq)
wave3 = osc(freq * 1.005)
```

---

### Success Criteria

The synth sounds:
- wider
- warmer
- more alive

---

## Step 4 — Add Stereo Rendering

### Goal

Convert mono rendering into stereo rendering.

---

### Example

```python
stereo = np.column_stack([left, right])
```

---

### Success Criteria

You can:
- pan sounds
- create width
- hear stereo movement

---

## Step 5 — Add Basic Effects

### Goal

Create reusable effect processors.

---

### First Effects

Implement ONLY:
- delay
- reverb
- lowpass filter

Ignore everything else initially.

---

### Suggested Interface

```python
processed = effect.process(audio)
```

---

### Success Criteria

You can:
- chain effects
- apply multiple effects
- hear clear differences

---

## Step 6 — Create a Basic Mixer

### Goal

Mix multiple rendered audio signals together.

---

### Example

```python
final = track1 + track2
```

---

### Success Criteria

You can:
- combine layers
- avoid clipping
- normalize output

---

## Step 7 — Render a Small Demo Track

### Goal

Create your first:

```text
small complete musical render
```

---

### Requirements

Use:
- at least 2 layers
- ADSR
- detune
- stereo
- one effect

---

### Final Deliverable

A decent sounding rendered ambient/chiptune track.

---

# Recommended Stopping Point

STOP Phase 1 when:
- rendering works reliably
- audio sounds reasonably good
- the synth is reusable

DO NOT:
- chase realism
- optimize heavily
- build 40 effects

Move on.

---