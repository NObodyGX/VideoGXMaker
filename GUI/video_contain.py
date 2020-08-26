from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSplitter, QVBoxLayout, QWidget
from .video_player import VideoPlayer


class VideoContain(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()
        
    def init_ui(self):
        self.layout = QVBoxLayout()
        self.splitter = VideoContainSplitter()
        self.player = VideoPlayer()
        self.info = VideoInfo(self)
        self.splitter.addWidget(self.player)
        self.splitter.addWidget(self.info)
        self.splitter.setStretchFactor(0, 7)
        self.splitter.setStretchFactor(1, 3)
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)

    def init_function(self):
        pass


class VideoInfo(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.init_ui()
        self.init_function()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title = EditorLabel('标题', '', self)
        self.subtitle = EditorLabel('副标题', '', self)
        self.rank = EditorLabel('分级', 0, self)
        self.tag = EditorLabel('标记', '', self)
        self.note = EditorLabel('备注', 0, self)
        self.artis = EditorLabel('艺术家', 0, self)
        self.year = EditorLabel('年', 0, self)
        self.gene = EditorLabel('流派', 0, self)
        self.start = QPushButton('Start')

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.subtitle)
        self.layout.addWidget(self.rank)
        self.layout.addWidget(self.tag)
        self.layout.addWidget(self.note)
        self.layout.addWidget(self.artis)
        self.layout.addWidget(self.year)
        self.layout.addWidget(self.gene)
        self.layout.addWidget(self.start)
        self.setLayout(self.layout)
        self.show()

    def init_function(self):
        pass

    def read_info(self, file_path):
        pass

class EditorLabel(QWidget):
    def __init__(self, name, value, parent=None) -> None:
        super().__init__(parent)
        self.init_ui(name, value)
        self.init_function()
    
    def init_ui(self, name, value):
        self.layout = QHBoxLayout()
        self.label = QLabel(name, parent=self)
        self.label.setFixedWidth(80)
        self.edit = QLineEdit(str(value), parent=self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.edit)
        self.setLayout(self.layout)
        self.show()
    
    def init_function(self):
        pass

    def setText(self, text):
        self.edit.setText(text)


class VideoContainSplitter(QSplitter):
    pass
