# Oscillate — Complete Development Roadmap

> A long-term roadmap and architecture guide for building a visually expressive modular music creation environment.
>
> This document is written for:
>
> * future-you
> * current-you
> * contributors
> * learning-by-building
>
> The goal is NOT to compete with professional DAWs.
>
> The goal IS:
>
> * understanding audio systems
> * learning synthesis
> * building your own ecosystem
> * creating expressive visuals
> * creating a functional self-made DAW
>
> Philosophy:
>
> ```text
> Build cool things that teach you things.
> ```

---

# Core Vision

Oscillate is NOT:

* a clone of FL Studio
* a clone of Ableton
* an industry-focused production suite

Oscillate IS:

* a personal DAW
* a visual music creation environment
* a modular synth playground
* a procedural experimentation platform
* a long-term systems project

The project should prioritize:

1. interaction
2. visualization
3. modularity
4. experimentation
5. sound quality
6. realism

---



# OVERALL DEVELOPMENT TIMELINE

# Phase 1 — Stabilize Core Audio Engine


# Phase 2 — Event-Based Sequencing


# Phase 3 — Piano Roll GUI



# Phase 4 — Project Save/Load System


# Phase 5 — Instrument & Effect System


# Phase 6 — Audio Visualizer System


# Phase 7 — Modular Node Graph System



# Phase 8 — Procedural & Scripting Systems



# Phase 9 — Real-Time Systems (Later)


# Suggested Learning Resources

# GUI

## PyQt6

Research:

* signals/slots
* QGraphicsScene
* custom widgets
* layouts

---

# DSP

## Books

* Think DSP
* The Scientist and Engineer's Guide to DSP

## Topics

* filtering
* FFT
* convolution
* modulation

---

# Music Theory

Focus ONLY on:

* intervals
* chord construction
* chord progressions
* rhythm

You do NOT need deep theory early.

---

# MOST IMPORTANT PROJECT ADVICE

## DO NOT CHASE INDUSTRY STANDARDS

Your goal is:

```text
self-owned expressive software
```

not:

```text
professional commercial DAW
```

That distinction matters enormously.

---

# Your First Major Milestones

## Milestone 1

```text
Render decent synth audio.
```

(already partially complete)

---

## Milestone 2

```text
Build event-based sequencing.
```

---

## Milestone 3

```text
Create a piano roll GUI.
```

THIS is the first truly massive milestone.

---

## Milestone 4

```text
Save/load editable projects.
```

---

## Milestone 5

```text
Render a complete song with visuals.
```

THIS is likely your:

```text
holy shit i built this
```

moment.

---

# Phase 2 Detailed Design — Event System Architecture

## Why This Phase Matters

This phase is the foundation of the entire DAW.

Right now the engine works like this:

```python
melody = [
    ("A4", 0.5),
    ("C5", 1.0),
]
```

This works for:

* experiments
* small demos
* testing synthesis

But it breaks down immediately when you need:

* overlapping notes
* piano rolls
* looping
* quantization
* layered instruments
* automation
* project editing

This phase converts the engine into a REAL sequencing system.

---

# Core Idea

Instead of:

```text
notes as ordered audio generation
```

Use:

```text
notes as timed data events
```

Audio becomes a RESULT of rendering data.

This distinction is incredibly important.

---

# Recommended Core Data Model

## NoteEvent

```python
class NoteEvent:
    def __init__(
        self,
        note,
        start,
        duration,
        velocity=1.0,
    ):
        self.note = note
        self.start = start
        self.duration = duration
        self.velocity = velocity
```

---

## Clip

A clip is a container of note events.

Examples:

* drum loop
* melody phrase
* chord section

```python
class Clip:
    def __init__(self, name="Clip"):
        self.name = name
        self.notes = []
```

---

## Track

Tracks contain:

* clips
* instruments
* effects

```python
class Track:
    def __init__(self, name="Track"):
        self.name = name
        self.clips = []
        self.instrument = None
        self.effects = []
```

---

## Project

Top-level container.

```python
class Project:
    def __init__(self):
        self.bpm = 120
        self.tracks = []
```

---

# Recommended Timing System

## IMPORTANT

Use:

```text
beats
```

NOT:

```text
seconds
```

internally.

Reason:

* music is beat-based
* BPM changes become possible
* quantization becomes easier
* piano rolls become simpler

---

# Example

Instead of:

```python
start = 2.36
```

Use:

```python
start_beat = 4.0
```

Then convert:

```python
seconds = beats * 60 / bpm
```

---

# Quantization

Quantization means:

```text
snap notes to rhythmic grid positions
```

Example:

```text
1/4 notes
1/8 notes
1/16 notes
```

---

# Recommended Render Pipeline

## Current

```text
generate note arrays
→ concatenate
```

---

## New

```text
project
    ↓
tracks
    ↓
clips
    ↓
note events
    ↓
renderer
    ↓
audio buffer
```

---

# Timeline Rendering Example

Pseudo-code:

```python
for note in clip.notes:
    rendered = instrument.render(note)

    start = beat_to_sample(note.start)
    end = start + len(rendered)

    buffer[start:end] += rendered
```

This is the core idea behind most DAWs.

---

# Recommended Early Features

## MUST HAVE

* overlapping notes
* beat-based timing
* looping
* velocity
* multiple tracks

## DO LATER

* automation
* tempo changes
* swing/groove
* MIDI import/export

---

# Suggested Folder Structure

```text
app/sequencing/
    note_event.py
    clip.py
    track.py
    project.py
    renderer.py
```

---

# Suggested Learning Checkpoint

By the end of this phase you should understand:

* sequencing
* timeline rendering
* audio scheduling
* beat-based timing
* overlapping synthesis
* project data models

---

# Common Beginner Mistakes

## 1. Mixing GUI logic with audio logic

Avoid:

```text
GUI directly generating sound
```

Instead:

```text
GUI edits project data
renderer generates sound
```

---

## 2. Storing generated audio everywhere

Store:

```text
music data
```

NOT:

```text
tons of permanent wave arrays
```

---

## 3. Hardcoding instrument logic into tracks

Tracks should reference instruments.

NOT contain synthesis code directly.

---

# Phase 3 Detailed Design — Piano Roll Architecture

## Why This Phase Matters

This is where Oscillate stops feeling like:

```text
python scripts
```

and starts feeling like:

```text
music software
```

This phase is psychologically huge.

---

# Recommended Stack

## GUI

```text
PyQt6
```

## Graphics

```text
QGraphicsScene
QGraphicsView
```

These are PERFECT for piano rolls.

---

# Core Piano Roll Concept

```text
X-axis = time
Y-axis = pitch
```

Each note becomes:

```text
a draggable rectangle
```

---

# Recommended Architecture

## VERY IMPORTANT

The piano roll should NOT contain musical logic.

The piano roll should:

```text
visualize and edit project data
```

ONLY.

---

# Recommended GUI Structure

```text
MainWindow
 ├── TimelineHeader
 ├── PianoRollView
 ├── TrackPanel
 ├── TransportControls
 └── InspectorPanel
```

---

# Recommended First Features

## Essential

* note drawing
* note dragging
* note resizing
* play button
* playback cursor
* zooming
* snapping

## Ignore Initially

* fancy themes
* animations
* plugins
* automation lanes
* MIDI recording

---

# Recommended Rendering Strategy

Each note rectangle should reference:

```python
NoteEvent
```

Example:

```python
class PianoRollNote(QGraphicsRectItem):
    def __init__(self, note_event):
        self.note_event = note_event
```

Then moving the note:

```text
updates the data model
```

NOT just the visual.

---

# Coordinate System Example

## Time

```python
x = beat * pixels_per_beat
```

## Pitch

```python
y = (max_pitch - midi_note) * note_height
```

This is basically how piano rolls work internally.

---

# Playback Cursor

The playback cursor is simply:

```text
a moving vertical line
```

whose position depends on:

```python
current_beat
```

---

# Recommended Interaction Features

## Left Click

Create note.

## Drag

Move note.

## Resize Edge

Change duration.

## Right Click

Delete note.

---

# Recommended Future Features

## Later Add:

* velocity editing
* multiple clips
* automation lanes
* color coding
* piano keyboard sidebar
* ghost notes
* fold-to-scale

---

# Suggested GUI Folder Structure

```text
app/gui/
    main_window.py
    piano_roll.py
    timeline.py
    transport.py
    track_panel.py
```

---

# Important Concepts To Research

## PyQt6

Research:

* signals and slots
* QGraphicsScene
* QGraphicsItem
* QPainter
* event handling

---

## DAW Piano Rolls

Study:

* FL Studio
* Ableton
* Reaper
* LMMS

Pay attention to:

* zooming
* note editing
* snapping
* playback cursor behavior

---

# Suggested First Visual Milestone

```text
Draw notes on a piano roll
→ press play
→ hear your own synth
→ watch playback cursor move
```

THIS is the first major emotional milestone of the project.

---

# Final Reminder

The goal is not perfection.

The goal is:

* exploration
* interaction
* systems
* creativity
* understanding

You are building:

```text
a visual music laboratory
```

And honestly?

That is far more interesting than cloning a commercial DAW.
