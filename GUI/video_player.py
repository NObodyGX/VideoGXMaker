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
        self.play_button = SwitchButton('play',  self.play, 'pause', self.pause)
        self.stop_button = StopButton('stop', self.stop)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.player_view)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.stop_button)
        self.setLayout(self.layout)
        self.show()

    def init_function(self):
        self.setAcceptDrops(True)

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

class Button(QPushButton):
    def __init__(self, text, func) -> None:
        super().__init__(text)
        self.clicked.connect(func)

class SwitchButton(QPushButton):
    def __init__(self, aText, aFunc, bText, bFunc) -> None:
        super().__init__(aText)
        self.aText = aText
        self.bText = bText
        self.aFunc = aFunc
        self.bFunc = bFunc
        self.count = 0
        self.clicked.connect(self._func)
    
    def _func(self):
        self.count += 1
        if self.count % 2 == 1:
            self.aFunc()
            self.setText(self.bText)
            return
        self.bFunc()
        self.setText(self.aText)

class StopButton(Button):
    pass


