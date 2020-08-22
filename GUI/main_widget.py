from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, Qt
from .title_bar import TitleBar
from .video_widget import VideoWidget

class MainWidget(QFrame):

    window_min_single = pyqtSignal()
    window_max_single = pyqtSignal()
    window_close_single = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()
    
    def init_ui(self):
        self.layout = QVBoxLayout()
        self.title = TitleBar(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.title)
        self.layout.addSpacing(5)
        self.video = VideoWidget(self)
        self.layout.addWidget(self.video)
        self.setLayout(self.layout)
        self.show()

    def init_function(self):
        self.title.window_min_single.connect(self.window_min)
        self.title.window_max_single.connect(self.window_max)
        self.title.window_close_single.connect(self.window_close)

    def set_max_icon(self, isMax):
        self.title.set_max_icon(isMax)

    def window_min(self):
        self.window_min_single.emit()

    def window_max(self):
        self.window_max_single.emit()

    def window_close(self):
        self.window_close_single.emit()
    
    def title_rect(self):
        return self.title.rect()
    
    def resizeEvent(self, e: QResizeEvent) -> None:
        super().resizeEvent(e)
