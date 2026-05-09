# Phase 3 — Piano Roll GUI

# Phase 3 Execution Plan

## Goal

Create the first TRUE music interaction layer.

This phase transforms Oscillate from:

```text
python project
```

into:

```text
music software
```

---

# IMPORTANT

DO NOT try to build a full DAW immediately.

Build:

```text
minimal but functional piano roll
```

ONLY.

---

# Recommended Development Order

## Step 1 — Create Main Window

### Goal

Create the base PyQt application.

---

### Success Criteria

You can:
- open the app
- show panels
- render basic UI

---

### Files

```text
app/gui/main_window.py
```

---

## Step 2 — Create Static Piano Roll Grid

### Goal

Draw:
- horizontal pitch lines
- vertical beat lines

---

### Important Concept

```text
X-axis = time
Y-axis = pitch
```

---

### Success Criteria

You can:
- scroll timeline
- zoom timeline
- visualize beat spacing

---

## Step 3 — Draw Static Notes

### Goal

Render note events visually.

---

### Example

```python
QGraphicsRectItem
```

---

### Success Criteria

You can:
- visualize notes
- map note timing to X
- map pitch to Y

---

## Step 4 — Add Playback Cursor

### Goal

Visualize current playback position.

---

### Success Criteria

You can:
- animate cursor movement
- sync playback visually
- follow timeline position

---

## Step 5 — Add Note Creation

### Goal

Click to place notes.

---

### Success Criteria

You can:
- create notes visually
- update project data
- hear new notes after render

---

## Step 6 — Add Dragging & Resizing

### Goal

Edit notes visually.

---

### Success Criteria

You can:
- drag notes
- resize notes
- snap notes to grid

---

## Step 7 — Add Transport Controls

### Goal

Add:
- play
- stop
- BPM controls

---

### Success Criteria

You can:
- control playback
- restart playback
- change tempo

---

## Step 8 — Render Directly From GUI State

### Goal

Connect GUI editing to renderer.

---

### IMPORTANT

The GUI should:

```text
edit project data
```

NOT:

```text
generate sound directly
```

---

### Success Criteria

You can:
- draw notes
- press play
- hear synth
- watch playback cursor move

---

# FIRST MAJOR EMOTIONAL MILESTONE

```text
Draw notes
→ press play
→ hear your own synth
→ watch your own piano roll animate
```

THIS is where the project becomes real.

---

# Recommended Stopping Point

STOP Phase 3 when:
- editing feels usable
- playback works visually
- notes can be edited comfortably

Ignore:
- themes
- plugins
- advanced visuals
- automation

Focus ONLY on:
- interaction
- editing
- workflow

---