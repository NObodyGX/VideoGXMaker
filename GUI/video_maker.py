from PyQt5.QtWidgets import QFrame, QVBoxLayout



class VideoMaker(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        self.init_function()
        
    def init_ui(self):
        pass

    def init_function(self):
        pass