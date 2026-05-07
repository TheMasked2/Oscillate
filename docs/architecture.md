# Recommended Tech Stack

## Current Stack

* Python
* NumPy
* Offline rendering

## Recommended Near-Future Stack

### GUI

* PyQt6
* pyqtgraph

### Audio

* sounddevice
* scipy.signal
* NumPy

### Serialization

* JSON

### Visualization

* pyqtgraph
* OpenGL later
* shaders later

---

# Important Architectural Principles

## 1. Separate DATA from AUDIO

This is extremely important.

Example:

BAD:

```python
track.waveform = generated_audio
```

BETTER:

```python
Track(
    instrument="pad_1",
    notes=[...],
    effects=[...]
)
```

Then:

```text
Renderer converts data into audio.
```

This allows:

* save/load
* undo systems
* automation
* re-rendering
* visual editing
* procedural systems

---

## 2. Build Vertical Slices

Do NOT build:

```text
all DSP first
```

Build:

```text
small complete systems
```

Example:

* one synth
* one piano roll
* one render button
* one visualizer

This creates momentum.

---

## 3. Keep It Modular

Every major system should eventually become replaceable.

Example:

```text
Instrument
    ↓
Effect Chain
    ↓
Mixer
    ↓
Visualizer
```

NOT:

```text
massive monolithic audio file
```

---

## 4. Slow but Understandable > Fast but Confusing

Do NOT optimize too early.

You are learning systems.

Readable architecture matters more than performance right now.

---

# Recommended Repository Structure

```text
Oscillate/
│
├── app/
│   ├── audio/
│   ├── engine/
│   ├── gui/
│   ├── visuals/
│   ├── instruments/
│   ├── effects/
│   ├── sequencing/
│   ├── rendering/
│   ├── serialization/
│   ├── plugins/
│   └── utils/
│
├── docs/
│   ├── roadmap.md
│   ├── architecture.md
│   ├── concepts/
│   └── phases/
│
├── projects/
├── tests/
├── examples/
└── assets/
```

---