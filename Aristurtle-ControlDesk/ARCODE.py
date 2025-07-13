# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from mainWindow import Mainwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Mainwindow()
    MainWindow.show()
    # ...
    sys.exit(app.exec())