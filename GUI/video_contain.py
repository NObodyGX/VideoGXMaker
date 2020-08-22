from PyQt5.QtWidgets import QFrame, QHBoxLayout, QSplitter, QVBoxLayout



class VideoContain(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()
        
    def init_ui(self):
        self.layout = QVBoxLayout()
        self.splitter = VideoContainSplitter()
        self.player = VideoPlayer(self)
        self.info = VideoInfo(self)
        self.splitter.addWidget(self.player)
        self.splitter.addWidget(self.info)
        self.splitter.setStretchFactor(0, 7)
        self.splitter.setStretchFactor(1, 3)
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)

    def init_function(self):
        pass


class VideoContainSplitter(QSplitter):
    pass


class VideoPlayer(QFrame):
    pass


class VideoInfo(QFrame):
    pass