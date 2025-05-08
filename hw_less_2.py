import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("HomeWork_2")
        self.setGeometry(200, 200, 350, 250)
        self.label = QLabel("Текст ДО таймера", self)
        self.label.move(125, 100)

        self.label2 = QLabel("Текст ПОСЛЕ таймера", self)
        self.label2.move(125, 100)
        self.label2.hide()

        QTimer.singleShot(2000, self.show_label)

    def show_label(self):
        self.label.hide()
        self.label2.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
