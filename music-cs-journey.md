# Music Theory + Computer Science Learning Journey
**16-Week Evening & Weekend Program**

---

## Timeline Overview

**Time Commitment:** 8-12 hours/week
- Weeknights: 1-2 hours (theory, small experiments)
- Weekends: 4-6 hours (main coding projects)

---

## Phase 1: Audio Fundamentals + Simple Synth (Weeks 1-5)

### Week 1-2: Sound Basics & First Sounds
**Weeknight Focus:**
- Read about sound waves, frequency, amplitude
- Watch Sebastian Lague's sound visualization videos
- Learn basic music theory (notes, octaves)

**Weekend Project:**
- Set up Python audio environment
- Generate your first sine wave
- Create a simple melody player

**Theory Topics:**
- What is sound? (physics basics)
- Digital audio (sample rate, bit depth)
- Musical notes and frequency relationships

### Week 3-4: Harmony Through Code
**Weeknight Focus:**
- Learn intervals (minor 3rd, major 3rd, perfect 5th, etc.)
- Study chord construction (triads, 7th chords)
- Analyze "Just Overture" chord progressions

**Weekend Project:**
- Build "Harmony Explorer" tool
- Chord generator functions
- Play and hear different chord types

**Theory Topics:**
- Intervals and their emotional qualities
- Major, minor, diminished, augmented chords
- Chord progressions basics

### Week 5: Mini-Project Week
**Weekend Focus:**
- Build playable keyboard synth
- Multiple waveform types (sine, square, saw, triangle)
- Basic envelope (ADSR) implementation

---

## Phase 2: Visualization Magic (Weeks 6-10)

### Week 6-7: Waveform Visualization
**Weeknight Focus:**
- Learn matplotlib/pygame basics
- Study oscilloscope principles
- Plan visualization architecture

**Weekend Project:**
- Real-time waveform display
- Oscilloscope-style viewer
- Connect to your synth from Phase 1

**Concepts:**
- Time domain representation
- Buffering and real-time display
- Graphics optimization

### Week 8-9: Frequency Domain (Spectrum Analysis)
**Weeknight Focus:**
- Learn FFT (Fast Fourier Transform) theory
- Study frequency spectrum concepts
- Watch tutorials on spectrum analyzers

**Weekend Project:**
- Build spectrum analyzer with frequency bars
- Frequency vs amplitude visualization
- Color-coded frequency bands

**Concepts:**
- Fourier analysis basics
- Frequency bins and resolution
- Harmonics and overtones

### Week 10: Creative Visuals
**Weekend Focus:**
- Lissajous curves (X-Y mode oscilloscope)
- Circular/radial visualizers
- Particle systems responding to audio
- Audio-reactive animations

**Explore:**
- Different mapping strategies (amplitude → size, frequency → color)
- Combining multiple visualization types
- Recording/exporting visualizations

---

## Phase 3: DAW World + Plugin Development (Weeks 11-14)

### Week 11-12: Cakewalk Deep Dive
**Weeknight Focus:**
- Install and explore Cakewalk
- Learn basic MIDI concepts
- Study signal flow and routing
- Watch mixing tutorials

**Weekend Projects:**
- Create a simple track using Cakewalk
- Learn basic mixing (levels, panning, EQ)
- Use your Python synth to generate MIDI/audio
- Import and arrange in Cakewalk

**DAW Concepts:**
- MIDI vs Audio tracks
- Virtual instruments and effects
- Automation
- Basic mixing principles

### Week 13-14: Plugin Development / Advanced Integration
**Choose your path:**

**Option A - Python MIDI Tools:**
- Generate MIDI files programmatically
- Create algorithmic composition tools
- Python scripts that interact with Cakewalk

**Option B - C# / JUCE Plugin:**
- Set up JUCE framework
- Build simple gain/filter VST plugin
- Learn plugin architecture basics

**Weekend Projects:**
- Create a useful tool for music production
- Integrate your visualizations with DAW workflow

---

## Phase 4: Integration Project (Weeks 15-16)

**Choose ONE capstone project:**

1. **Audio-Visual Performance Tool**
   - Real-time visualization system
   - Responds to live audio input or DAW output
   - Multiple visualization modes

2. **Intelligent Harmony Assistant**
   - Analyzes piano recordings
   - Suggests complementary synth parts
   - Visualizes harmonic relationships

3. **Custom Synthesizer + Visualizer**
   - Full-featured synth with GUI
   - Built-in visualization panel
   - Save/load presets

4. **Live Coding Music Environment**
   - Code-based music creation
   - Real-time parameter control
   - Integrated visualization

---

## Ongoing Visualization Techniques

### Basics (Weeks 1-7)
- **Waveform Display:** Time domain oscilloscope view
- **Volume Meters:** VU meters, peak meters
- **Simple Shapes:** Circles/bars that pulse with sound

### Intermediate (Weeks 8-12)
- **Spectrum Analyzer:** Frequency bars (like Winamp)
- **Spectrogram:** Time + frequency heatmap
- **Lissajous Curves:** Phase relationship visualization
- **Circular Waveforms:** Polar coordinate displays
- **Piano Roll Visualization:** MIDI note display

### Advanced (Weeks 13-16)
- **3D Visualizations:** Frequency × time × amplitude
- **Harmonic Analyzers:** Show overtone series
- **Chromagram:** Musical note/chord tracker
- **Audio-Reactive Generative Art:** Fractals, particles
- **Music Notation Generation:** Convert audio to sheet music
- **Chord/Harmony Visualizer:** Real-time chord recognition

---

# Resources & Sources

## Sebastian Lague References
- [Sound and Visualization](https://www.youtube.com/watch?v=nxKm2ARiA3M) - Core concepts
- [Coding Adventure: Sound](https://www.youtube.com/watch?v=9w3o7hPNgY0) - Synthesis approach

## Music Reference
- **Aloboi - Just Overture** - Study this for harmony examples
  - Listen for: chord progressions, layered synths, harmonic movement

---

## Python Audio Libraries

### Essential Libraries
- **numpy** - Array manipulation, waveform generation
  - Documentation: https://numpy.org/doc/
  - Tutorial: https://numpy.org/doc/stable/user/quickstart.html

- **sounddevice** - Real-time audio I/O
  - GitHub: https://github.com/spatialaudio/python-sounddevice
  - Documentation: https://python-sounddevice.readthedocs.io/

- **pyaudio** - Alternative audio library
  - Documentation: https://people.csail.mit.edu/hubert/pyaudio/

- **scipy** - Scientific computing (includes signal processing)
  - Audio tools: https://docs.scipy.org/doc/scipy/reference/io.html
  - Signal processing: https://docs.scipy.org/doc/scipy/reference/signal.html

### Visualization
- **matplotlib** - Plotting and visualization
  - Real-time plotting: https://matplotlib.org/stable/users/explain/animations/animations.html
  - Documentation: https://matplotlib.org/

- **pygame** - Game library (good for interactive visuals)
  - Documentation: https://www.pygame.org/docs/
  - Tutorial: https://www.pygame.org/wiki/tutorials

- **pyqtgraph** - Fast real-time plotting
  - Documentation: http://pyqtgraph.org/

### Music-Specific
- **music21** - Music theory analysis toolkit
  - Documentation: http://web.mit.edu/music21/
  - Great for: analyzing chords, scales, progressions

- **mido** - MIDI file handling
  - Documentation: https://mido.readthedocs.io/
  - Tutorial: https://mido.readthedocs.io/en/latest/midi_files.html

- **pretty_midi** - MIDI manipulation
  - GitHub: https://github.com/craffel/pretty-midi

---

## Music Theory (Coder-Friendly)

### Books
- **"Music Theory for Computer Musicians"** by Michael Hewitt
  - Perfect balance of theory and practical application
  - Covers harmony, scales, chord progressions
  - Available: Amazon, PDF versions online

- **"Hooktheory I & II"**
  - Interactive, visual approach to music theory
  - Website: https://www.hooktheory.com/
  - Great for understanding chord progressions

### Online Courses & Tutorials
- **Learning Music (by Ableton)** - FREE
  - https://learningmusic.ableton.com/
  - Interactive, visual, beginner-friendly
  - Covers beats, notes, scales, chords

- **Music Theory for Songwriting (Coursera)**
  - Berklee College course
  - https://www.coursera.org/learn/music-theory-songwriting

- **Andrew Huang YouTube Channel**
  - Accessible music theory concepts
  - https://www.youtube.com/user/andrewhuang

### Quick References
- **teoria.com** - Interactive music theory lessons
  - https://www.teoria.com/

- **musictheory.net** - Comprehensive free lessons
  - https://www.musictheory.net/

---

## Synthesis & Sound Design

### Interactive Learning
- **Syntorial** - Interactive synthesis course (PAID but excellent)
  - https://www.syntorial.com/
  - Learn-by-doing approach
  - Covers subtractive synthesis deeply

- **Learning Synths (by Ableton)** - FREE
  - https://learningsynths.ableton.com/
  - Interactive web-based lessons
  - Covers oscillators, envelopes, LFOs, filters

### Books
- **"Designing Sound"** by Andy Farnell
  - Procedural audio approach
  - Uses Pure Data (visual programming)
  - Theory-heavy but excellent

- **"The Computer Music Tutorial"** by Curtis Roads
  - Comprehensive academic text
  - Deep dive into synthesis, DSP, computer music

### Video Tutorials
- **In The Mix** - Synthesis basics
  - https://www.youtube.com/c/inthemix
  - Clear explanations of synthesis concepts

- **SeamlessR** - Sound design tutorials
  - https://www.youtube.com/user/SeamlessR
  - FL Studio focused but concepts apply everywhere

---

## Digital Signal Processing (DSP)

### Beginner-Friendly
- **"The Scientist and Engineer's Guide to Digital Signal Processing"**
  - FREE online book: http://www.dspguide.com/
  - Chapter 22-23 are especially relevant for audio

- **3Blue1Brown - Fourier Transform**
  - Visual explanation: https://www.youtube.com/watch?v=spUNpyF58BY
  - Excellent intuitive understanding

### Python-Specific
- **"Think DSP"** by Allen Downey - FREE
  - http://greenteapress.com/wp/think-dsp/
  - Python-based DSP introduction
  - Code examples included

### YouTube Channels
- **The Audio Programmer**
  - https://www.youtube.com/c/TheAudioProgrammer
  - C++ focused but concepts apply
  - Plugin development tutorials

- **Valerio Velardo (The Sound of AI)**
  - https://www.youtube.com/c/ValerioVelardoTheSoundofAI
  - Audio + AI/ML
  - Python implementations

---

## Visualization Techniques

### Tutorials
- **Processing.org** - Visual coding environment
  - https://processing.org/
  - Great for generative art and audio-reactive visuals
  - Has Python mode (p5py)

- **The Coding Train** (Daniel Shiffman)
  - Sound visualization: https://www.youtube.com/user/shiffman
  - Creative coding tutorials
  - Processing and p5.js

- **Audio Visualization with Python**
  - Tutorial series: https://python.plainenglish.io/making-audio-visualizer-with-python-5e677c5f6ba9

### Tools & Libraries
- **p5.py** - Python version of Processing
  - http://p5py.github.io/

- **nannou** - Creative coding in Rust (advanced)
  - https://nannou.cc/

---

## DAW: Cakewalk

### Official Resources
- **Cakewalk by BandLab** - FREE DAW
  - Download: https://www.bandlab.com/products/cakewalk
  - Fully featured, professional DAW
  - Windows only

### Tutorials
- **Creative Sauce YouTube**
  - Cakewalk tutorials: https://www.youtube.com/c/CreativeSauce
  - Beginner to advanced

- **Audio Tech TV**
  - Cakewalk-specific content
  - https://www.youtube.com/c/AudioTechTV

- **Official Cakewalk Documentation**
  - https://www.cakewalk.com/Documentation

### Free Plugins for Cakewalk
- **TAL Plugins** - Free synths and effects
  - https://tal-software.com/products
  - TAL-NoiseMaker (great free synth)

- **Spitfire LABS** - Free instruments
  - https://labs.spitfireaudio.com/

- **Valhalla Supermassive** - Free reverb
  - https://valhalladsp.com/shop/reverb/valhalla-supermassive/

---

## Plugin Development

### JUCE Framework (C++)
- **JUCE Official Site**
  - https://juce.com/
  - Industry-standard framework
  - Cross-platform VST/AU/AAX

- **JUCE Tutorials**
  - Official: https://docs.juce.com/master/tutorial_simple_synth_noise.html
  - The Audio Programmer YouTube (mentioned above)

- **"Getting Started with JUCE"** by Martin Robinson
  - Book: https://www.packtpub.com/product/getting-started-with-juce/9781783283071

### Python Alternatives
- **pyo** - Python DSP library
  - http://ajaxsoundstudio.com/software/pyo/
  - Can create standalone audio apps

- **DAWG** - Python VST wrapper (experimental)
  - GitHub: https://github.com/hq9000/py_headless_daw

---

## Advanced/Specialized Tools

### Live Coding
- **Sonic Pi** - Live coding music
  - https://sonic-pi.net/
  - Ruby-based, beginner-friendly
  - Built-in synths and samples

- **TidalCycles** - Algorithmic patterns
  - https://tidalcycles.org/
  - Haskell-based
  - Advanced but powerful

### Pure Data / Max/MSP
- **Pure Data (Pd)** - Visual programming for audio
  - FREE: http://puredata.info/
  - Learning: https://puredata.info/docs/tutorials/

- **Max/MSP** - Professional visual programming
  - https://cycling74.com/products/max
  - PAID but very powerful
  - Free trial available

---

## YouTube Channels (Comprehensive List)

### Music Production
- **Andrew Huang** - Creative music making
- **Busy Works Beats** - Production tutorials
- **In The Mix** - Mixing and production

### Synthesis & Sound Design
- **SeamlessR** - Advanced sound design
- **Syntorial** - Synthesis education
- **Au5** - Technical sound design

### Music Theory
- **Adam Neely** - Music theory deep dives
- **12tone** - Visual music theory analysis
- **David Bennett Piano** - Harmony analysis

### Code + Music
- **The Coding Train** - Creative coding
- **The Audio Programmer** - Audio software development
- **Valerio Velardo** - AI + Audio

### Math/Science of Music
- **3Blue1Brown** - Mathematical explanations
- **Welch Labs** - Fourier series explained

---

## Communities & Forums

### Reddit
- **/r/musictheory** - Theory discussions
- **/r/synthrecipes** - Sound design
- **/r/audioengineering** - Technical audio
- **/r/WeAreTheMusicMakers** - General production
- **/r/Python** - Python help
- **/r/learnprogramming** - Coding help

### Discord Servers
- **The Audio Programmer Discord** - DSP and plugin dev
- **Cakewalk Users** - DAW-specific help

### Stack Exchange
- **Music: Practice & Theory** - https://music.stackexchange.com/
- **Signal Processing** - https://dsp.stackexchange.com/
- **Stack Overflow** - General programming

---

## Week-by-Week Reading/Watching Plan

### Weeks 1-2
- [ ] Sebastian Lague sound videos (both)
- [ ] Learning Music (Ableton) - Complete all sections
- [ ] "Think DSP" - Chapters 1-3
- [ ] Set up Python environment with numpy, sounddevice

### Weeks 3-4
- [ ] Learning Synths (Ableton) - Complete
- [ ] Musictheory.net - Intervals and Chords sections
- [ ] Watch: 3Blue1Brown Fourier Transform
- [ ] Start "Music Theory for Computer Musicians" - Chapters 1-4

### Weeks 5-7
- [ ] The Coding Train - Sound visualization tutorials
- [ ] Pygame documentation - Graphics basics
- [ ] Continue "Music Theory for Computer Musicians" - Chapters 5-8
- [ ] Experiment with matplotlib animations

### Weeks 8-10
- [ ] "Think DSP" - Chapters 4-7 (FFT and filtering)
- [ ] Processing.org - Audio tutorials
- [ ] The Audio Programmer - FFT visualization videos

### Weeks 11-12
- [ ] Install Cakewalk and explore interface
- [ ] Creative Sauce - Cakewalk beginner series
- [ ] Official Cakewalk tutorials - Signal flow
- [ ] In The Mix - Basic mixing tutorials

### Weeks 13-14
- [ ] Choose path: Python MIDI OR JUCE plugins
- [ ] If JUCE: The Audio Programmer plugin tutorials
- [ ] If Python: mido documentation and examples
- [ ] Plan your integration project

### Weeks 15-16
- [ ] Build capstone project
- [ ] Revisit any concepts that need reinforcement
- [ ] Document your journey
- [ ] Share your work!

---

## Bonus: Connection Projects

Ideas to bridge your world with classical piano:

1. **Piano Chord Analyzer**
   - Record her playing
   - Visualize the chord progressions
   - Show harmonic analysis

2. **Classical + Synth Arranger**
   - Take classical piece MIDI
   - Generate complementary synth parts
   - Visualize harmonic relationships

3. **Practice Tool**
   - Chord progression trainer
   - Interval recognition game
   - Scale practice visualizer

4. **Performance Visualizer**
   - Real-time visual response to piano
   - Create "visual scores" of her performances
   - Beautiful gift and shows you understand her art

---

## Tips for Success

### Time Management
- **Weeknights (1-2 hours):**
  - Reading/watching (30-45 min)
  - Small coding experiments (30-45 min)
  - Theory practice (15-30 min)

- **Weekends (4-6 hours):**
  - Main project work (3-4 hours)
  - Experimentation and play (1-2 hours)

### Learning Strategies
- Code along with tutorials, don't just watch
- Keep a "sound journal" - document what you learn
- Share progress (with her, on Reddit, wherever)
- Don't rush - absorption matters more than speed
- It's okay to spend extra time on interesting topics

### When You Get Stuck
1. Break the problem into smaller pieces
2. Search for specific error messages
3. Ask on relevant subreddits/forums
4. Revisit fundamentals
5. Take a break and come back fresh

---

## Next Steps

1. **This Week:** Set up your Python environment
2. **First Weekend:** Generate your first sound
3. **By End of Month:** Have a working simple synth
4. **Keep me updated:** Share your progress, questions, and discoveries!

---

**Remember:** This journey is about building bridges between your passions and understanding her world through your unique lens. The technical skills are valuable, but the creative exploration is what makes this meaningful.

Good luck! 🎹🎵💻
