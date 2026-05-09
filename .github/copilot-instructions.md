# Oscillate — Copilot Project Instructions

## Project Overview

Oscillate is a long-term learning-focused visual music creation environment.

The goal is NOT:
- competing with professional DAWs
- enterprise-level abstraction
- premature optimization
- perfect realism

The goal IS:
- understanding synthesis
- understanding DAW architecture
- learning DSP concepts
- building modular systems
- creating expressive visual music tools
- experimentation and exploration
- building a personal self-made DAW

Oscillate combines:
- synthesis
- sequencing
- visualization
- procedural systems
- modular audio architecture
- GUI interaction
- creative coding

This project should feel:
- educational
- modular
- visually expressive
- understandable
- extensible


---

# Development Philosophy

## PRIORITY ORDER

1. clean architecture
2. modularity
3. clarity/readability
4. experimentation
5. optimization

If optimization conflicts with readability:
- choose readability first.

Only optimize obvious bottlenecks.


---

# Architecture Rules

## VERY IMPORTANT

Each function/class should have ONE responsibility.

GOOD:
```python
generate_wave()
apply_adsr()
mix_tracks()
```

BAD:
```python
generate_and_play_audio()
```

Strong separation of concerns is REQUIRED.

---

# Required Separation

GUI:
- edits project state
- visualizes data
- NEVER generates audio directly

Renderer:
- converts project state into audio
- NEVER manages GUI state

Sequencing:
- manages timing and note placement
- NEVER handles visualization

Effects:
- process audio only
- should remain modular and chainable

Instruments:
- generate audio only
- should not manage playback/UI

Models/Core Data:
- should remain pure data structures
- no rendering logic
- no GUI logic


---

# Current Project Direction

Current roadmap focus:
- event sequencing
- timeline rendering
- piano roll architecture
- modular audio systems

DO NOT:
- introduce advanced real-time threading
- over-engineer plugin systems
- introduce unnecessary enterprise patterns
- optimize prematurely

Focus on:
- understandable architecture
- reusable systems
- visual interaction
- maintainability


---

# Coding Style

## General Style

Prefer:
- short clear functions
- readable variable names
- explicit logic
- modular files

Avoid:
- giant files
- magic abstractions
- hidden behavior
- unnecessary inheritance
- deeply nested logic

Keep files reasonably small and focused.

If a file becomes too large:
- suggest splitting responsibilities.


---

# Abstraction Rules

Core systems should be reusable.

Feature-specific logic can remain explicit until repetition naturally appears.

DO NOT create abstraction layers “just in case”.

Abstractions should emerge naturally from repeated patterns.


---

# Dependency Philosophy

Prefer:
- Python standard library
- NumPy
- lightweight dependencies

Avoid adding dependencies unless:
- they significantly improve architecture
- they solve a real bottleneck
- they meaningfully improve usability


---

# GUI Philosophy

GUI polish is NOT the priority.

Priority order:
1. functionality
2. usability
3. maintainability
4. visuals/styling

Prefer:
- modular widgets
- reusable UI components
- maintainable layouts

Avoid:
- giant monolithic windows
- tightly coupled UI logic
- styling-heavy implementations early


---

# DSP / Audio Philosophy

Prefer:
- understandable DSP implementations
- educational clarity
- experimentation-friendly code

Do NOT:
- aggressively optimize DSP early
- introduce extremely advanced DSP concepts too early
- hide important DSP logic behind abstractions

Leave TODO comments for:
- future optimizations
- future improvements
- possible extensions


---

# Documentation Style

Use:
- concise docstrings
- short architecture comments
- TODO sections for future improvements

Comments should explain:
- WHY something exists
- architectural intent
- important constraints

Avoid excessive comment clutter.


---

# Desired Copilot Behavior

Act like:
- a senior engineer mentor
- a guide/teacher
- a collaborative systems designer

Encourage:
- experimentation
- learning
- modularity
- architectural consistency

When requirements are unclear:
- ask clarifying questions
- avoid silently changing architecture

When suggesting code:
- explain tradeoffs briefly
- prefer understandable solutions
- leave extension points where useful


---

# Preferred Programming Style

Use:
- object-oriented data models
- procedural rendering/audio processing

Examples:

GOOD:
```python
class NoteEvent:
    ...
```

```python
render_project(project)
```

Avoid:
- excessive inheritance trees
- overly generic frameworks
- “smart” hidden systems


---

# Important Project Concepts

Oscillate is evolving toward:
- a piano roll DAW
- modular synthesis
- procedural composition systems
- reactive visuals
- custom plugins/effects
- visual audio experimentation

The project is intended to grow incrementally through:
- vertical slices
- functional milestones
- iterative experimentation


---

# IMPORTANT

If architecture decisions become ambiguous:
- ask for clarification
- do not invent major systems silently

Maintain consistency with:
- modularity
- separation of concerns
- learning-focused design
- experimentation-friendly architecture


---

# Current Milestone

Current implementation priority:
1. event system
2. timeline renderer
3. piano roll GUI

Focus suggestions around these systems first.