from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent, QWheelEvent
from PyQt5.QtWidgets import QFrame, QGroupBox, QHBoxLayout, QLabel, QSpinBox, QVBoxLayout, QWidget
from Utils.delay_decorator import Delayer


class VideoMaker(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()
        
    def init_ui(self):
        self.layout = QHBoxLayout()
        self.input_group = QGroupBox('Input')
        self.input_timer = TimerSpin()
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input_timer)
        self.input_layout.addStretch()
        self.input_group.setLayout(self.input_layout)
        self.layout.addWidget(self.input_group)

        self.output_group = QGroupBox('Output')
        self.output_format = QLabel()
        self.output_layout = QHBoxLayout()
        self.output_layout.addWidget(self.output_format)
        self.output_group.setLayout(self.output_layout)
        self.layout.addWidget(self.output_group)
        self.setLayout(self.layout)
        self.show()

    def init_function(self):
        pass


class TimerSpin(QFrame):
    def __init__(self, ) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.z = 0
        self.init_ui()
        self.init_function()
    
    def init_ui(self):
        self.layout = QHBoxLayout()
        self.xWidget = Spin(self)
        self.yWidget = Spin(self)
        self.zWidget = Spin(self)
        self.layout.addWidget(self.xWidget)
        self.layout.addWidget(self.yWidget)
        self.layout.addWidget(self.zWidget)
        self.setLayout(self.layout)
        self.show()
    
    def init_function(self):
        pass


class ClockSpin(QSpinBox):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setMinimum(0)
        self.setMaximum(60)
        self.setSingleStep(1)


class Spin(QLabel):
    def __init__(self, parent=None, default=0, min=0, max=60) -> None:
        super().__init__(parent)
        self.__value = 0
        self.__left_button_stay = False
        self.__right_button_stay = False
        self.default = default
        self.min = min
        self.max = max
        self.value = self.default
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, v):
        if v >= self.min and v <= self.max:
            self.__value = int(v)
        if self.value < 10:
            self.setText(' ' + str(self.__value))
            return
        self.setText(str(self.__value))
    
    def setValue(self, value):
        """
        供外部使用接口
        """
        self.value = value

    def wheelEvent(self, e: QWheelEvent) -> None:
        if e.angleDelta().y() > 0:
            self.value += 1
        else:
            self.value -= 1

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.value += 1
            self.__left_button_stay = True
            self.left_button_check()
        elif e.button() == Qt.RightButton:
            self.value -= 1
            self.__right_button_stay = True
            self.right_button_check()
        elif e.button() == Qt.MidButton:
            self.value = self.defaultValue

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.__left_button_stay = False
        elif e.button() == Qt.RightButton:
            self.__right_button_stay = False

    @Delayer.delay(0.2)
    def left_button_check(self):
        """
        每0.2秒检测一次是否在按下状态
        """
        if self.__left_button_stay:
            self.value += 1
            self.left_button_check()
    
    @Delayer.delay(0.2)
    def right_button_check(self):
        """
        每0.2秒检测一次是否在按下状态
        """
        if self.__right_button_stay:
            self.value -= 1
            self.right_button_check()


class Template(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()
    
    def init_ui(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.show()
    
    def init_function(self):
        pass
