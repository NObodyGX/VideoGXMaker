from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSplitter, QVBoxLayout, QWidget
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaBindableInterface, QMediaContent, QMediaPlayer


class VideoPlayer(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.label = QLabel('empty!!!')
        self.player_view = QVideoWidget(self)
        self.player_view.show()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.player_view)
        self.pause_button = PauseButton('pause')
        self.play_button = PauseButton('play')
        self.stop_button = PauseButton('stop')
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.player_view)
        self.layout.addWidget(self.pause_button)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.stop_button)
        self.setLayout(self.layout)
        self.show()

    def init_function(self):
        self.setAcceptDrops(True)
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)

    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        if e.mimeData().text():
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e: QDropEvent) -> None:
        file_path = e.mimeData().text().replace('file:///', '')
        self.label.setText(file_path)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.player.play()

    def play(self):
        self.player.play()
    
    def pause(self):
        self.player.pause()
    
    def stop(self):
        self.player.stop()

class PauseButton(QPushButton):
    pass

class PlayButton(QPushButton):
    pass

class StopButton(QPushButton):
    pass


