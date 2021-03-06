from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QAction, QFrame, QMenu, QPushButton, QLabel, QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QPoint, Qt, pyqtSignal


class TitleBar(QFrame):

    window_min_single = pyqtSignal()
    window_max_single = pyqtSignal()
    window_close_single = pyqtSignal()


    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.init_ui()
        self.init_function()
    
    def init_ui(self):
        self.layout = QHBoxLayout()
        self.setFixedHeight(30)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.label = TitleLabel('Title')
        self.file_menu = FileMenu('File')
        self.start_menu = FileMenu('start')
        self.help_menu = FileMenu('help')
        self.about_menu = FileMenu('about')
        self.min_button = MinButton('min')
        self.max_button = MaxButton('max')
        self.close_button = CloseButton('close')
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.file_menu)
        self.layout.addWidget(self.start_menu)
        self.layout.addWidget(self.help_menu)
        self.layout.addWidget(self.about_menu)
        self.layout.addStretch(1)
        self.layout.addWidget(self.min_button)
        self.layout.addStretch(0)
        self.layout.addWidget(self.max_button)
        self.layout.addStretch(0)
        self.layout.addWidget(self.close_button)
        self.setLayout(self.layout)
        self.show()

    def init_function(self):
        self.min_button.clicked.connect(self.window_min)
        self.max_button.clicked.connect(self.window_max)
        self.close_button.clicked.connect(self.window_close)

    def window_min(self):
        self.window_min_single.emit()

    def window_max(self):
        self.window_max_single.emit()

    def window_close(self):
        self.window_close_single.emit()
    
    def set_max_icon(self, isMax):
        if isMax:
            self.max_button.setText('normal')
            return
        self.max_button.setText('max')

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.window_max()


class MinButton(QPushButton):
    pass

class MaxButton(QPushButton):
    pass

class CloseButton(QPushButton):
    pass

class TitleLabel(QPushButton):
    pass

class TitleMenu(QLabel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def global_pos(self):
        x = self.frameGeometry().x()
        y = self.frameGeometry().y()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        return self.mapToGlobal(QPoint(x - width - 8, y + height))


class FileMenu(TitleMenu):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
