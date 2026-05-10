import time

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
)
from PyQt6.QtCore import QTimer, Qt

from ..playback.player import Player
from ..audio.mixer import Mixer
from ..core.project import Project
from ..core.track import Track
from ..core.clip import Clip
from ..core.note_event import NoteEvent
from ..gui.arrangement_workspace import ArrangementWorkspace


def build_demo_project():
    project = Project("Oscillate DAW")

    lead_track = Track("Lead", instrument="triangle", volume=0.9)
    bass_track = Track("Bass", instrument="sine", volume=0.8)
    pad_track = Track("Pad", instrument="piano", volume=0.7)

    project.add_track(lead_track)
    project.add_track(bass_track)
    project.add_track(pad_track)

    melody = [
        ("A4", 0.5),
        ("C5", 0.5),
        ("E5", 1.0),
        ("G5", 0.5),
        ("E5", 1.0),
        ("D5", 0.5),
        ("C5", 0.5),
        ("E5", 1.0),
        ("A5", 0.5),
        ("G5", 1.0),
        ("E5", 0.5),
        ("C5", 0.5),
        ("D5", 1.0),
    ]

    bassline = [
        ("A2", 2.0),
        ("F2", 2.0),
        ("C3", 2.0),
        ("G2", 2.0),
    ]

    lead_clip = Clip("Lead Phrase", start_time=0.0, duration=12.0)

    cursor = 0.0
    for pitch, duration in melody:
        lead_clip.add_note_event(
            NoteEvent(
                pitch,
                velocity=100,
                start_time=cursor,
                duration=duration,
            )
        )
        cursor += duration

    lead_track.add_clip(lead_clip)

    bass_clip = Clip("Bass Phrase", start_time=0.0, duration=8.0)

    cursor = 0.0
    for pitch, duration in bassline:
        bass_clip.add_note_event(
            NoteEvent(
                pitch,
                velocity=100,
                start_time=cursor,
                duration=duration,
            )
        )
        cursor += duration

    bass_track.add_clip(bass_clip)

    pad_clip = Clip("Pad", start_time=4.0, duration=8.0)

    pad_clip.add_note_event(
        NoteEvent(
            "C4",
            velocity=100,
            start_time=0.0,
            duration=8.0,
        )
    )

    pad_track.add_clip(pad_clip)

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

        self.setWindowTitle("Oscillate — DAW")

        self._build_ui()

    def _build_ui(self):
        central_widget = QWidget()

        central_widget.setStyleSheet(
            """
            background: #10131a;
            color: #e8eaea;
            font-family: Segoe UI;
            """
        )

        self.setCentralWidget(central_widget)

        root = QVBoxLayout()
        root.setContentsMargins(8, 8, 8, 8)
        root.setSpacing(8)

        top_bar = QHBoxLayout()
        top_bar.setSpacing(10)

        tools = QLabel("TOOLS")
        tools.setFixedWidth(210)
        tools.setStyleSheet(
            "color: #9ccfd8; font-weight: bold;"
        )

        top_bar.addWidget(tools)

        top_bar.addStretch(1)

        self.play_button = QPushButton("▶")
        self.pause_button = QPushButton("⏸")
        self.stop_button = QPushButton("⏹")
        self.loop_button = QPushButton("🔁")

        buttons = [
            self.play_button,
            self.pause_button,
            self.stop_button,
            self.loop_button,
        ]

        for button in buttons:
            button.setFixedSize(32, 32)
            button.setStyleSheet(
                """
                QPushButton {
                    background: #1f2430;
                    border: 1px solid #2f3650;
                    color: #f4f7fb;
                }

                QPushButton:hover {
                    background: #283042;
                }
                """
            )

        self.play_button.clicked.connect(self.on_play)
        self.pause_button.clicked.connect(self.on_pause)
        self.stop_button.clicked.connect(self.on_stop)

        top_bar.addWidget(self.play_button)
        top_bar.addWidget(self.pause_button)
        top_bar.addWidget(self.stop_button)
        top_bar.addWidget(self.loop_button)

        bpm_label = QLabel(f"BPM: {self.project.settings.tempo}")
        bpm_label.setStyleSheet("color: #d0d7ff;")

        # position_label = QLabel("Pos: 1 | 1 | 1")
        # position_label.setStyleSheet("color: #c8d1e8;")

        # top_bar.addWidget(bpm_label)
        # top_bar.addWidget(position_label)

        top_bar.addStretch(1)

        right_placeholder = QLabel("")
        right_placeholder.setFixedWidth(210)

        top_bar.addWidget(right_placeholder)

        root.addLayout(top_bar)

        middle = QHBoxLayout()
        middle.setSpacing(10)

        browser = QLabel("BROWSER")
        browser.setAlignment(Qt.AlignmentFlag.AlignTop)
        browser.setFixedWidth(210)

        browser.setStyleSheet(
            """
            background: #151a22;
            border: 1px solid #243044;
            padding: 14px;
            color: #b8c2d6;
            """
        )

        middle.addWidget(browser)

        self.arrangement = ArrangementWorkspace(
            self.project,
            beat_width=88,
            lane_height=92,
            control_width=240,
        )

        middle.addWidget(self.arrangement, 1)

        root.addLayout(middle, 1)

        bottom_panel = QLabel("DEVICES / CLIP SETTINGS")

        bottom_panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bottom_panel.setFixedHeight(160)

        bottom_panel.setStyleSheet(
            """
            background: #151a22;
            border: 1px solid #243044;
            color: #b8c2d6;
            """
        )

        root.addWidget(bottom_panel)

        central_widget.setLayout(root)

    def _player_is_playing(self):
        play_check = getattr(self.player, "is_playing", None)
        if callable(play_check):
            return play_check()
        return bool(getattr(self.player, "is_playing", False))

    def _player_is_paused(self):
        paused = getattr(self.player, "is_paused", None)
        if callable(paused):
            return paused()
        return bool(paused)

    def _player_duration(self):
        return getattr(self.player, "duration", None)

    def _player_position(self):
        return getattr(self.player, "current_position", None)

    def on_play(self):
        if self._player_is_paused():
            self.player.resume()
        else:
            self.player.play()

        self.play_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.play_timer.start()

    def on_pause(self):
        if self._player_is_playing():
            self.player.pause()
            self.pause_button.setText("Resume")
            self.play_timer.stop()
            return

        if self._player_is_paused():
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
        self.arrangement.set_playhead_position(0.0)

    def _update_playhead(self):
        if not self._player_is_playing():
            self.on_stop()
            return

        position = self._player_position()
        duration = self._player_duration()

        if position is None:
            return

        if duration is not None and position >= duration:
            self.on_stop()
            return

        self.arrangement.set_playhead_position(position)


def main():
    import sys

    app = QApplication(sys.argv)

    project = build_demo_project()

    window = MainWindow(project)
    window.resize(1600, 900)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()