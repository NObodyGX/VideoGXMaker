from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow
from PyQt5.QtCore import QPoint, Qt
from .main_widget import MainWidget


class MainWindow(QMainWindow):
    _startPos = None
    _endPos = None
    _isTracking = False
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.init_function()
    
    def init_ui(self):
        self.resize(1200, 720)
        self.setWindowTitle('Simple')
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.widget = MainWidget()
        self.setCentralWidget(self.widget)
        
        self.status = self.statusBar()
        self.status.showMessage('正在初始化...', 1000)
        self.center()
    
    def init_function(self):
        self.widget.window_min_single.connect(self.window_min)
        self.widget.window_max_single.connect(self.window_max)
        self.widget.window_close_single.connect(self.window_close)
        
    def window_min(self):
        self.showMinimized()

    def window_max(self):
        if self.isMaximized():
            self.showNormal()
            self.widget.set_max_icon(False)
            return
        self.showMaximized()
        self.widget.set_max_icon(True)

    def window_close(self):
        self.close()
    
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) /2 )
    
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._isTracking and self._startPos is not None and e.pos() in self.widget.title_rect():
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
 
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._isTracking = True
 
    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None