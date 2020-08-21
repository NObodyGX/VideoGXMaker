import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from GUI.main_window import MainWindow
from Utils.qss_helper import QssHelper



if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.getcwd(), './GUI/Qss/style.qss')
    main_window = MainWindow()
    main_window.show()
    main_window.setStyleSheet(QssHelper.load(qss_path))
    sys.exit(app.exec_())
