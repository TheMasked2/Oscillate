import time

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QGraphicsView,
    QGraphicsScene,
)
from PyQt6.QtGui import QBrush, QColor, QPen, QPainter
from PyQt6.QtCore import Qt, QTimer

from .piano_roll import PianoRollView
from ..playback.player import Player
from ..audio.mixer import Mixer
from ..core.project import Project
from ..core.track import Track
from ..core.clip import Clip
from ..core.note_event import NoteEvent

def build_demo_project():
    melody = [
        ("A4", 0.5),
        ("C5", 0.5),
        ("E5", 1.0),
        ("rest", 0.5),
        ("G5", 0.5),
        ("E5", 1.0),
        ("D5", 0.5),
        ("C5", 0.5),
        ("E5", 1.0),
        ("rest", 0.5),
        ("A5", 0.5),
        ("G5", 1.0),
        ("E5", 0.5),
        ("C5", 0.5),
        ("D5", 1.0),
        ("rest", 0.5),
        ("E5", 0.5),
        ("G5", 1.0),
        ("A5", 0.5),
        ("G5", 0.5),
        ("E5", 1.0),
        ("rest", 0.5),
        ("C5", 0.5),
        ("A4", 1.0),
    ]

    bassline = [
        ("A2", 2.0),
        ("F2", 2.0),
        ("C3", 2.0),
        ("G2", 2.0),
        ("F2", 2.0),
        ("C3", 2.0),
        ("G2", 2.0),
        ("A2", 2.0),
    ]

    project = Project("Oscillate-alpha-0.1")

    lead_track = Track("lead", instrument="triangle", volume=1.0)
    bass_track = Track("bass", instrument="sine", volume=0.9)

    lead_clip = Clip("lead_phrase", start_time=0.0, duration=sum(duration for _, duration in melody))
    time_cursor = 0.0
    for pitch, duration in melody:
        lead_clip.add_note_event(NoteEvent(pitch, velocity=100, start_time=time_cursor, duration=duration))
        time_cursor += duration
    lead_track.add_clip(lead_clip)

    bass_clip = Clip("bass_phrase", start_time=0.0, duration=sum(duration for _, duration in bassline))
    time_cursor = 0.0
    for pitch, duration in bassline:
        bass_clip.add_note_event(NoteEvent(pitch, velocity=110, start_time=time_cursor, duration=duration))
        time_cursor += duration
    bass_track.add_clip(bass_clip)

    project.add_track(lead_track)
    project.add_track(bass_track)

    return project

class MainWindow(QMainWindow):
    def __init__(self, project):
        super().__init__()
        self.project = project
        self.mixer = Mixer(project)
        self.player = Player(mixer=self.mixer)
        self.play_timer = QTimer(self)
        self.play_timer.setInterval(30)
        self.play_timer.timeout.connect(self._update_playhead)

        self.setWindowTitle("Oscillate — Piano Roll")
        self._build_ui()

    def _build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        controls = QHBoxLayout()

        self.info_label = QLabel(f"BPM: {self.project.settings.tempo}")
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.pause_button.setEnabled(False)
        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)

        self.play_button.clicked.connect(self.on_play)
        self.pause_button.clicked.connect(self.on_pause)
        self.stop_button.clicked.connect(self.on_stop)

        controls.addWidget(self.info_label)
        controls.addStretch()
        controls.addWidget(self.play_button)
        controls.addWidget(self.pause_button)
        controls.addWidget(self.stop_button)

        self.piano_roll = PianoRollView(self.project)

        layout.addLayout(controls)
        layout.addWidget(self.piano_roll)
        central_widget.setLayout(layout)

    def on_play(self):
        if self.player.is_paused:
            self.player.resume()
        else:
            self.player.play()

        if self.player.audio_buffer is not None and self.player.audio_buffer.size > 0:
            self.play_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            self.play_timer.start()

    def on_pause(self):
        if self.player.is_playing():
            self.player.pause()
            self.pause_button.setText("Resume")
            self.play_timer.stop()
        elif self.player.is_paused:
            self.player.resume()
            self.pause_button.setText("Pause")
            self.play_timer.start()

    def on_stop(self):
        self.player.stop()
        self.play_button.setEnabled(True)
        self.pause_button.setText("Pause")
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.play_timer.stop()
        self.piano_roll.set_playhead_position(0.0)

    def _update_playhead(self):
        if not self.player.is_playing():
            self.on_stop()
            return

        position = self.player.current_position
        if position >= self.player.duration:
            self.on_stop()
            return

        self.piano_roll.set_playhead_position(position)

def main():
    import sys

    app = QApplication(sys.argv)
    project = build_demo_project()
    window = MainWindow(project)
    window.resize(1280, 720)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()