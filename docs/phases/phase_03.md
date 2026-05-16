# Phase 3 — Piano Roll GUI & Interactive Clip Workflow

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
minimal but functional clip-based piano roll workflow
```

ONLY.

---

# IMPORTANT REALIZATION

A professional DAW does NOT place raw notes directly onto tracks.

Professional DAWs use:

```text
Tracks
→ Clips
→ Note Events
```

NOT:

```text
Tracks
→ Notes
```

This abstraction is VERY important.

---

# Core Workflow Goal

The user should eventually be able to:

```text
1. create track
2. create clip
3. open clip editor
4. place notes
5. press play
6. hear playback
7. watch playhead movement
8. edit notes interactively
```

THIS is the first real DAW milestone.

---

# Recommended Development Order

# Step 1 — Create Main Window

## Goal

Create the base PyQt application.

---

## Success Criteria

You can:

* open the app
* show panels
* render basic UI

---

## Files

```text
app/gui/main_window.py
```

---

# Step 2 — Create Static Piano Roll Grid

## Goal

Draw:

* horizontal pitch lines
* vertical beat lines

---

## Important Concept

```text
X-axis = time
Y-axis = pitch
```

---

## Success Criteria

You can:

* scroll timeline
* zoom timeline
* visualize beat spacing

---

# Step 3 — Draw Static Notes

## Goal

Render note events visually.

---

## Example

```python
QGraphicsRectItem
```

---

## Success Criteria

You can:

* visualize notes
* map note timing to X
* map pitch to Y

---

# Step 4 — Add Playback Cursor

## Goal

Visualize current playback position.

---

## Success Criteria

You can:

* animate cursor movement
* sync playback visually
* follow timeline position

---

# IMPORTANT ARCHITECTURE SHIFT

At this point the project transitions from:

```text
visual note editor
```

into:

```text
real clip-based DAW workflow
```

The next steps replace the original simplistic:

```text
track directly contains notes
```

architecture.

From this point onward:

```text
Tracks
→ contain Clips
→ Clips contain NoteEvents
```

---

# Step 5 — Add Track Creation

## Goal

Allow users to create tracks dynamically.

---

## Requirements

Add:

```text
+ Add Track
```

button.

Tracks should contain:

* name
* clips
* volume
* mute state
* solo state

---

## Success Criteria

You can:

* create tracks
* visualize tracks
* manage track state

---

# Step 6 — Create Clip Data Structure

## Goal

Introduce proper clip abstraction.

---

## Files

```text
app/sequencing/clip.py
```

---

## Example Structure

```python
class Clip:
    start_beat: float
    length_beats: float
    notes: list[NoteEvent]
```

---

## Responsibilities

Clips should:

* contain note events
* define playback region
* support resizing later
* support looping later

---

## Success Criteria

You can:

* create clips
* store clips on tracks
* serialize clips later

---

# Step 7 — Create Arrangement View

## Goal

Render clips visually on tracks.

---

## IMPORTANT

Arrangement view should render:

```text
clips
```

NOT:

```text
individual notes
```

---

## Requirements

Visualize:

* track lanes
* clip blocks
* timeline grid
* beat markers

---

## Success Criteria

You can:

* see clips
* understand song structure
* visualize timing clearly

---

# Step 8 — Add Clip Creation

## Goal

Allow users to create clips interactively.

---

## Example Interaction

```text
double click empty track area
```

creates:

```python
Clip(
    start_beat=4,
    length_beats=4,
)
```

---

## IMPORTANT

Default clip lengths are completely acceptable initially.

Resizable clips come later.

---

## Success Criteria

You can:

* create clips visually
* place clips on tracks
* update arrangement dynamically

---

# Step 9 — Create Clip Editor / Piano Roll

## Goal

Create the FIRST true MIDI editing interface.

---

## IMPORTANT

The piano roll should:

```text
edit ONE selected clip
```

NOT:

```text
the entire arrangement
```

---

## Recommended Behavior

When:

```text
double clicking a clip
```

Open:

```text
clip editor
```

inside:

* bottom panel
  OR
* dedicated editor area

similar to Ableton Live.

---

## Success Criteria

You can:

* select clips
* open clip editor
* edit notes independently

---

# Step 10 — Add Note Creation

## Goal

Allow interactive MIDI editing.

---

## Requirements

User can:

* click to create notes
* place notes on grid
* update clip note data

---

## IMPORTANT

The GUI edits:

```python
NoteEvent(...)
```

objects.

NOT audio directly.

---

## Success Criteria

You can:

* place notes
* visualize notes
* save notes inside clips

---

# Step 11 — Add Real-Time Playback Scheduler

## Goal

Create continuous playback engine.

---

## Responsibilities

Scheduler handles:

* BPM timing
* playhead position
* note triggering
* looping
* playback state

---

## Example API

```python
scheduler.play()
scheduler.stop()

scheduler.current_beat
```

---

## IMPORTANT

This system becomes:

* the heartbeat of the DAW
* the source of timing
* the source of playback synchronization

---

## Success Criteria

You can:

* press play
* stop playback
* advance timeline continuously

---

# Step 12 — Connect Scheduler To Clips

## Goal

Playback notes from clips automatically.

---

## Playback Flow

```text
Scheduler
→ reads tracks
→ reads clips
→ triggers NoteEvents
→ synth generates audio
```

---

## Success Criteria

You can:

* press play
* hear clip playback
* hear notes at correct timing

---

# Step 13 — Add Immediate Audio Feedback

## Goal

Make editing feel interactive.

---

## Requirements

When:

* clicking notes
* placing notes
* editing notes

You immediately hear sound.

---

## IMPORTANT

This massively improves:

* experimentation
* usability
* creative workflow
* emotional feedback

---

## Success Criteria

Editing feels:

* responsive
* interactive
* musical

---

# Step 14 — Add Dragging & Resizing

## Goal

Create the first TRUE editing workflow.

---

## Requirements

Support:

* note dragging
* note resizing
* snapping to beat grid
* note selection

---

## Success Criteria

You can:

* compose visually
* adjust timing naturally
* iterate quickly

---

# Step 15 — Add Transport Controls

## Goal

Add:

* play
* stop
* pause
* BPM controls
* loop toggle

---

## Success Criteria

You can:

* control playback
* restart playback
* change tempo
* loop sections

---

# IMPORTANT ARCHITECTURE RULE

The GUI should:

```text
edit project data
```

NOT:

```text
generate sound directly
```

Correct architecture:

```text
GUI
→ edits NoteEvents / Clips / Tracks
→ scheduler reads project state
→ renderer produces sound
```

This separation is VERY important.

---

# FIRST MAJOR EMOTIONAL MILESTONE

```text
create track
→ create clip
→ open piano roll
→ place notes
→ press play
→ hear your synth
→ watch playback move
```

THIS is where the project becomes real.

---

# Recommended Stopping Point

STOP Phase 3 when:

* editing feels usable
* playback feels responsive
* notes can be edited comfortably
* clip workflow feels natural

Ignore:

* themes
* plugins
* advanced visuals
* automation
* orchestral realism
* advanced DSP

Focus ONLY on:

* clips
* playback
* editing
* timing
* interaction
* workflow
* audiovisual feedback

Because:

```text
interaction quality
is what makes creative software feel alive
```
