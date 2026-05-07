## Goal

Move toward live playback architecture.

THIS SHOULD NOT HAPPEN EARLY.

---

# Features

* streaming audio
* callback systems
* low-latency playback
* real-time automation
* live parameter changes

---

# Important Concepts To Research

* audio buffers
* threading
* synchronization
* latency
* audio callbacks

---

# LONG-TERM IDEAS

## AI Integration

Possible future features:

* melody generation
* harmony suggestions
* procedural visuals
* auto-layering
* sound design assistance

---

## Plugin Ecosystem

Possible future direction:

```text
/plugins
    my_reverb/
    my_pad_synth/
```

Potential future plugin API:

```python
class OscillatePlugin:
    def process(audio):
        pass
```

---

## Rendering Pipeline

Eventually:

```text
Project
    ↓
Renderer
    ↓
Audio Export
    ↓
Visualizer Export
```

---