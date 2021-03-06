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
        self.label = VideoTitle('empty!!!')
        self.begin_button = BeginButton('begin', self.begin)
        self.end_button = EndButton('end', self.end)
        self.player_view = QVideoWidget(self)
        self.player_view.show()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.player_view)
        self.play_button = SwitchButton('play',  self.play, 'pause', self.pause)
        self.stop_button = StopButton('stop', self.stop)
        self.next_button = NextFrameButton('next', self.next_frame)
        self.last_button = LastFrameButton('last', self.last_frame)

        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.label)
        self.title_layout.addWidget(self.begin_button)
        self.title_layout.addWidget(self.end_button)
        self.layout.addLayout(self.title_layout)
        self.layout.addWidget(self.player_view)
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.play_button)
        self.button_layout.addWidget(self.stop_button)
        self.button_layout.addWidget(self.next_button)
        self.button_layout.addWidget(self.last_button)
        self.button_layout.addStretch()
        self.layout.addLayout(self.button_layout)
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
        self.play_button.click()

    def play(self):
        self.player.play()
    
    def pause(self):
        self.player.pause()
    
    def stop(self):
        self.player.stop()
    
    def next_frame(self):
        # 这里的单位是毫秒
        position = self.player.position()
        self.player.setPosition(position + 1000)

    def last_frame(self):
        position = self.player.position()
        self.player.setPosition(position - 1000)

    def begin(self):
        pass

    def end(self):
        pass

class VideoTitle(QLabel):
    pass


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


class BeginButton(Button):
    pass

class EndButton(Button):
    pass

class StopButton(Button):
    pass


class NextFrameButton(Button):
    pass

class LastFrameButton(Button):
    pass

