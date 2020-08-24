from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QSplitter, QVBoxLayout, QWidget
from .video_maker import VideoMaker
from .video_contain import VideoContain


class VideoWidget(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.init_ui()
        self.init_function()
    
    def init_ui(self):
        """
        使用两个 splitter 无法调整外面一层的初始布局大小，这里额外增加一层
        """
        self.video_contain = VideoContain(self)
        main_splitter = VideoSplitter(Qt.Vertical)
        self.video_make = VideoMaker(self)
        main_splitter.addWidget(self.video_contain)
        main_splitter.addWidget(self.video_make)
        main_splitter.setStretchFactor(0, 7)
        main_splitter.setStretchFactor(1, 3)

        self.layout = QHBoxLayout()
        self.layout.addWidget(main_splitter)
        self.setLayout(self.layout)

        

    def init_function(self):
        pass


class VideoSplitter(QSplitter):
    pass

