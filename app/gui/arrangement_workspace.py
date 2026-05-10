from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QLabel,
    QSlider,
    QPushButton,
)
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QSize


class TimelineHeader(QWidget):
    def __init__(self, total_beats, beat_width, control_width, height=34, parent=None):
        super().__init__(parent)
        self.total_beats = max(1, int(total_beats))
        self.beat_width = beat_width
        self.control_width = control_width
        self._height = height

        self.setMinimumHeight(self._height)
        self.setMaximumHeight(self._height)

    def minimumSizeHint(self):
        return QSize(
            self.beat_width * (self.total_beats + 2) + self.control_width,
            self._height,
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#0f1318"))

        painter.setPen(QPen(QColor("#2d3440")))
        painter.drawLine(0, self.height() - 1, self.width(), self.height() - 1)

        font = QFont("Segoe UI", 9)
        painter.setFont(font)

        for beat in range(self.total_beats + 1):
            x = beat * self.beat_width

            painter.setPen(QPen(QColor("#2d3440")))
            painter.drawLine(x, 0, x, self.height())

            painter.setPen(QPen(QColor("#cbd3e6")))
            painter.drawText(x + 6, 20, str(beat + 1))


class ArrangementLane(QWidget):
    def __init__(self, track, total_width, beat_width, lane_height, parent=None):
        super().__init__(parent)

        self.track = track
        self.total_width = int(total_width)
        self.beat_width = beat_width
        self.lane_height = lane_height

        self.setMinimumWidth(self.total_width)
        self.setMinimumHeight(self.lane_height)
        self.setMaximumHeight(self.lane_height)

    def paintEvent(self, event):
        painter = QPainter(self)

        lane_color = QColor("#1a212b")
        painter.fillRect(self.rect(), lane_color)

        grid_pen = QPen(QColor("#2d3440"))
        painter.setPen(grid_pen)

        for beat_x in range(0, self.total_width, self.beat_width):
            painter.drawLine(beat_x, 0, beat_x, self.lane_height)

        painter.setPen(QPen(QColor("#202734")))
        painter.drawLine(0, self.lane_height - 1, self.total_width, self.lane_height - 1)

        clip_fill = QColor("#5d80bd")
        clip_border = QColor("#9ec0ff")

        for clip in getattr(self.track, "clips", []):
            clip_x = int(clip.start_time * self.beat_width)
            clip_width = max(10, int(clip.duration * self.beat_width))

            clip_y = 10
            clip_height = self.lane_height - 20

            painter.fillRect(
                clip_x,
                clip_y,
                clip_width,
                clip_height,
                clip_fill,
            )

            painter.setPen(QPen(clip_border))
            painter.drawRect(
                clip_x,
                clip_y,
                clip_width,
                clip_height,
            )

            painter.setPen(QPen(QColor("#eef4ff")))
            painter.drawText(clip_x + 8, clip_y + 18, clip.name)

            for note in getattr(clip, "note_events", []):
                note_x = clip_x + int(note.start_time * self.beat_width)
                note_width = max(8, int(note.duration * self.beat_width))

                note_y = clip_y + 26
                note_height = clip_height - 36

                painter.fillRect(
                    note_x,
                    note_y,
                    note_width,
                    note_height,
                    QColor("#87b3ff"),
                )

                painter.setPen(QPen(QColor("#d7e8ff")))
                painter.drawRect(
                    note_x,
                    note_y,
                    note_width,
                    note_height,
                )

                painter.drawText(
                    note_x + 6,
                    note_y + 16,
                    note.pitch,
                )


class TrackControlStrip(QWidget):
    def __init__(self, track, width=240, height=92, parent=None):
        super().__init__(parent)

        self.track = track

        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self._build_ui()
        self._refresh_button_states()

    def _build_ui(self):
        self.setStyleSheet(
            """
            background: #1a212b;
            border-left: 1px solid #2d3440;
            border-bottom: 1px solid #202734;
            """
        )

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 8, 12, 8)
        root.setSpacing(8)

        # ---------------------------
        # Track Name
        # ---------------------------

        self.track_name = QLabel(self.track.name)

        self.track_name.setStyleSheet(
            """
            color: #eef4ff;
            font-weight: bold;
            font-size: 11px;
            """
        )

        root.addWidget(self.track_name)

        # ---------------------------
        # Volume
        # ---------------------------

        volume_row = QHBoxLayout()
        volume_row.setSpacing(8)

        volume_label = QLabel("VOL")

        volume_label.setFixedWidth(28)

        volume_label.setStyleSheet(
            """
            color: #8d9bb3;
            font-size: 10px;
            """
        )

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)

        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(int(self.track.volume * 100))

        self.volume_slider.setStyleSheet(
            """
            QSlider::groove:horizontal {
                background: #2a3140;
                height: 4px;
                border-radius: 2px;
            }

            QSlider::sub-page:horizontal {
                background: #5eb7ff;
                border-radius: 2px;
            }

            QSlider::handle:horizontal {
                background: #dfe8ff;
                width: 12px;
                height: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            """
        )

        self.volume_slider.valueChanged.connect(
            self._on_volume_changed
        )

        volume_row.addWidget(volume_label)
        volume_row.addWidget(self.volume_slider)

        root.addLayout(volume_row)

        # ---------------------------
        # Buttons
        # ---------------------------

        controls = QHBoxLayout()
        controls.setSpacing(6)

        self.mute_button = QPushButton("M")
        self.solo_button = QPushButton("S")
        self.arm_button = QPushButton("R")

        self.mute_button.setCheckable(True)
        self.solo_button.setCheckable(True)
        self.arm_button.setCheckable(True)

        self.buttons = [
            self.mute_button,
            self.solo_button,
            self.arm_button,
        ]

        for button in self.buttons:
            button.setFixedSize(26, 26)

        self._apply_button_styles()

        self.mute_button.clicked.connect(self._toggle_mute)
        self.solo_button.clicked.connect(self._toggle_solo)
        self.arm_button.clicked.connect(self._toggle_arm)

        controls.addWidget(self.mute_button)
        controls.addWidget(self.solo_button)
        controls.addWidget(self.arm_button)
        controls.addStretch(1)

        root.addLayout(controls)

    def _apply_button_styles(self):
        self.mute_button.setStyleSheet(
            self._button_style(
                active=self.mute_button.isChecked(),
                active_color="#d97777",
            )
        )

        self.solo_button.setStyleSheet(
            self._button_style(
                active=self.solo_button.isChecked(),
                active_color="#d8b256",
            )
        )

        self.arm_button.setStyleSheet(
            self._button_style(
                active=self.arm_button.isChecked(),
                active_color="#e06060",
            )
        )

    def _button_style(self, active=False, active_color="#5eb7ff"):
        if active:
            return f"""
            QPushButton {{
                background: {active_color};
                border: 1px solid {active_color};
                color: #0f1318;
                font-weight: bold;
                border-radius: 3px;
            }}

            QPushButton:hover {{
                background: {active_color};
            }}
            """

        return """
        QPushButton {
            background: #202734;
            border: 1px solid #2f3850;
            color: #dfe7ff;
            border-radius: 3px;
        }

        QPushButton:hover {
            background: #283142;
        }
        """

    def _refresh_button_states(self):
        self._apply_button_styles()

        if getattr(self.track, "muted", False):
            self.track_name.setStyleSheet(
                """
                color: #8893a8;
                font-weight: bold;
                font-size: 11px;
                """
            )
        else:
            self.track_name.setStyleSheet(
                """
                color: #eef4ff;
                font-weight: bold;
                font-size: 11px;
                """
            )

    def _toggle_mute(self):
        self.track.toggle_mute()

        self.mute_button.setChecked(
            getattr(self.track, "muted", False)
        )

        self._refresh_button_states()

    def _toggle_solo(self):
        self._refresh_button_states()

    def _toggle_arm(self):
        self._refresh_button_states()

    def _on_volume_changed(self, value):
        self.track.set_volume(value / 100.0)


class TrackRowWidget(QWidget):
    def __init__(
        self,
        track,
        total_width,
        beat_width,
        lane_height,
        control_width=240,
        parent=None,
    ):
        super().__init__(parent)

        self.track = track

        self.total_width = total_width
        self.beat_width = beat_width
        self.lane_height = lane_height
        self.control_width = control_width

        self._build_ui()

    def _build_ui(self):
        self.setFixedHeight(self.lane_height)

        self.setStyleSheet(
            """
            background: #1a212b;
            border-bottom: 1px solid #202734;
            """
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.lane = ArrangementLane(
            self.track,
            total_width=self.total_width,
            beat_width=self.beat_width,
            lane_height=self.lane_height,
        )

        self.controls = TrackControlStrip(
            self.track,
            width=self.control_width,
            height=self.lane_height,
        )

        layout.addWidget(self.lane, 1)
        layout.addWidget(self.controls, 0)


class ArrangementWorkspace(QWidget):
    def __init__(
        self,
        project,
        beat_width=100,
        lane_height=92,
        control_width=240,
        parent=None,
    ):
        super().__init__(parent)

        self.project = project
        self.beat_width = beat_width
        self.lane_height = lane_height
        self.control_width = control_width

        self._build_ui()
        self.refresh()

    def _project_duration(self):
        max_end = 8.0

        for track in self.project.tracks:
            for clip in track.clips:
                max_end = max(max_end, clip.end_time)

        return max_end

    def _build_ui(self):
        self.setStyleSheet(
            """
            background: #0f1318;
            border: 1px solid #242b38;
            """
        )

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        total_beats = int(self._project_duration())

        self.header = TimelineHeader(
            total_beats,
            self.beat_width,
            self.control_width,
            height=34,
        )

        root.addWidget(self.header)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet(
            """
            background: #0f1318;
            border: none;
            """
        )

        root.addWidget(self.scroll, 1)

        self.content = QWidget()

        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        self.scroll.setWidget(self.content)

    def refresh(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        total_beats = int(self._project_duration())
        total_width = (total_beats + 2) * self.beat_width

        for track in self.project.tracks:
            row = TrackRowWidget(
                track,
                total_width=total_width,
                beat_width=self.beat_width,
                lane_height=self.lane_height,
                control_width=self.control_width,
            )

            self.content_layout.addWidget(row)

        self.content_layout.addStretch(1)

        self.content.setMinimumWidth(total_width + self.control_width)

    def set_playhead_position(self, time_seconds):
        x = int(time_seconds * self.beat_width)

        hbar = self.scroll.horizontalScrollBar()

        target = max(
            0,
            x - (self.scroll.viewport().width() // 3),
        )

        hbar.setValue(target)