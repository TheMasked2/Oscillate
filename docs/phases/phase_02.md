# Phase 2 — Event-Based Sequencing

# Phase 2 Execution Plan

## Goal

Convert the synth from:

```text
note list renderer
```

into:

```text
timeline-based sequencing engine
```

This is the foundation of the DAW.

---

# IMPORTANT

This phase matters MORE than:
- fancy synths
- effects
- visuals

because EVERYTHING later depends on it.

---

# Recommended Development Order

## Step 1 — Create NoteEvent

### Goal

Represent notes as reusable timeline objects.

---

### Example

```python
NoteEvent(
    note="C4",
    start=0.0,
    duration=1.0,
    velocity=0.8,
)
```

---

### Success Criteria

You can:
- create notes
- store timing
- store duration
- store velocity

---

### Files

```text
app/sequencing/note_event.py
```

---

## Step 2 — Create Clip

### Goal

Store multiple notes together.

---

### Example

```python
clip.notes.append(note)
```

---

### Success Criteria

You can:
- group notes
- iterate notes
- organize phrases

---

## Step 3 — Create Track

### Goal

Attach clips to instruments.

---

### Example

```python
track.instrument = pad_synth
```

---

### Success Criteria

You can:
- organize clips
- assign instruments
- prepare multi-track rendering

---

## Step 4 — Create Project

### Goal

Create top-level song structure.

---

### Example

```python
project.tracks.append(track)
```

---

### Success Criteria

You can:
- store BPM
- store tracks
- represent full songs

---

## Step 5 — Implement Beat Timing

### Goal

Use beats internally instead of seconds.

---

### Required Functions

```python
beat_to_seconds()
beat_to_sample()
```

---

### Success Criteria

You can:
- place notes musically
- change BPM globally
- calculate timing correctly

---

## Step 6 — Create Timeline Renderer

### Goal

Render note events into a timeline buffer.

---

### Example

```python
buffer[start:end] += rendered_note
```

---

### Success Criteria

You can:
- render arbitrary note positions
- overlap notes
- render clips
- render tracks

---

## Step 7 — Support Polyphony

### Goal

Allow multiple simultaneous notes.

---

### Success Criteria

You can:
- render chords
- overlap releases
- create layered music

---

## Step 8 — Render a Real Arrangement

### Goal

Create your first:

```text
multi-track arrangement
```

WITHOUT GUI.

Hardcode the project.

---

### Requirements

Use:
- multiple tracks
- overlapping notes
- different instruments
- effects

---

### Final Deliverable

A complete timeline-based render system.

---

# Recommended Stopping Point

STOP Phase 2 when:
- sequencing works reliably
- overlapping notes work
- timing feels correct
- BPM works globally

ONLY THEN:
- begin GUI work
- begin piano roll work

---