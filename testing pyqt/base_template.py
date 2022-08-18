from PyQt6 import QtWidgets as qtwid
from PyQt6 import QtCore as qtcore
from PyQt6 import QtGui as qtgui
import sys

class MainWindow(qtwid.QtWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = qtwid.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())