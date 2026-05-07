## Goal

Replace note concatenation with timeline scheduling.

THIS IS THE MOST IMPORTANT ARCHITECTURAL PHASE.

---

## Current System

```python
[("A4", 0.5)]
```

Problem:

* no overlapping notes
* no piano roll
* no automation
* no layering

---

## New System

```python
NoteEvent(
    note="A4",
    start=1.5,
    duration=0.75,
    velocity=0.8,
)
```

---

# Recommended Data Structures

```python
class NoteEvent:
    note: str
    start: float
    duration: float
    velocity: float
```

```python
class Clip:
    notes: list[NoteEvent]
```

```python
class Track:
    clips: list[Clip]
```

---

# Learning Goals

By the end of this phase you should understand:

* timeline rendering
* sequencing
* scheduling
* overlapping audio
* quantization
* project structure

---

# Deliverable

A timeline-based music system.

---

# Important Concepts To Research

## Piano Roll Logic

Research:

* MIDI timing
* note grids
* BPM
* beats vs seconds
* quantization

---

## Timeline Rendering

Example:

```python
buffer[start:end] += rendered_note
```

This becomes the core of the entire DAW.

---