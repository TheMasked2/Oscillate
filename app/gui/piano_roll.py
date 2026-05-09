from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QBrush, QColor, QPen, QPainter
from PyQt6.QtCore import Qt

from app.sequencing.sequencer import Sequencer

class PianoRollView(QGraphicsView):
    def __init__(self, project, parent=None):
        super().__init__(parent)
        self.project = project
        self.beat_width = 120
        self.track_height = 70
        self.note_height = 24
        self.track_spacing = 20
        self.playhead_x = 0.0
        self.playhead_line = None

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.refresh()

    def refresh(self):
        self.scene.clear()
        self._draw_grid()
        self._draw_notes()
        self._draw_playhead()

    def _draw_grid(self):
        sequencer = Sequencer(self.project)
        notes = sequencer.sequence()
        track_count = max(1, len(self.project.tracks))
        total_beats = max((note.end_time for note in notes), default=8.0)
        width = int((total_beats + 2) * self.beat_width)
        height = track_count * (self.track_height + self.track_spacing) + self.track_spacing

        self.setSceneRect(0, 0, width, height)

        grid_pen = QPen(QColor(220, 220, 220))
        for beat in range(int(total_beats) + 3):
            x = beat * self.beat_width
            self.scene.addLine(x, 0, x, height, grid_pen)

        for row in range(track_count + 1):
            y = row * (self.track_height + self.track_spacing)
            self.scene.addLine(0, y, width, y, grid_pen)

    def _draw_notes(self):
        sequencer = Sequencer(self.project)
        notes = sequencer.sequence()
        track_index_by_name = {track.name: index for index, track in enumerate(self.project.tracks)}

        for note in notes:
            track_index = track_index_by_name.get(note.track.name, 0)
            x = note.start_time * self.beat_width
            w = max(8.0, note.duration * self.beat_width)
            y = track_index * (self.track_height + self.track_spacing) + self.track_spacing

            self.scene.addRect(
                x,
                y,
                w,
                self.note_height,
                pen=QPen(Qt.GlobalColor.black),
                brush=QBrush(QColor(100, 180, 250, 180)),
            )
            label = self.scene.addText(str(note.pitch))
            label.setDefaultTextColor(Qt.GlobalColor.black)
            label.setPos(x + 4, y + 2)

    def _track_area_height(self):
        track_count = max(1, len(self.project.tracks))
        return track_count * (self.track_height + self.track_spacing) + self.track_spacing

    def _draw_playhead(self):
        track_area_height = self._track_area_height()
        pen = QPen(QColor(220, 50, 50), 2)
        if self.playhead_line is None:
            self.playhead_line = self.scene.addLine(
                self.playhead_x,
                0,
                self.playhead_x,
                track_area_height,
                pen,
            )
        else:
            self.playhead_line.setLine(
                self.playhead_x,
                0,
                self.playhead_x,
                track_area_height,
            )

    def set_playhead_position(self, time_seconds):
        self.playhead_x = time_seconds * self.beat_width
        self._draw_playhead()
        self.ensureVisible(self.playhead_x, 0, 200, self.scene.sceneRect().height())