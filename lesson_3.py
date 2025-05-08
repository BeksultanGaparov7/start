"""import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поле ввода")
        self.setGeometry(100, 100, 300, 200)

        self.input = QLineEdit(self)
        self.input.move(50, 50)

        self.label = QLabel("Введите что-нибудь:", self)
        self.label.move(50, 90)

        self.input.textChanged.connect(self.text_changed)

    def text_changed(self, text):
        self.label.setText(f"Вы ввели: {text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())"""


"""import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чекбокс")
        self.setGeometry(100, 100, 300, 200)

        self.checkbox = QCheckBox("Я согласен", self)
        self.checkbox.move(50, 50)

        self.label = QLabel("", self)
        self.label.move(50, 100)
        self.label.setWordWrap(True)
        self.label.resize(200, 50)

        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == 2:
            self.label.setText("Вы согласились!")
        else:
            self.label.setText("Вы не согласились!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QRadioButton
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('RadioButtons')
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon('home.ico'))

        self.r1 = QRadioButton('Variation1', self)
        self.r1.move(50,50)
        self.r2 = QRadioButton('Variation2', self)
        self.r2.move(50,80)

        self.label = QLabel('', self)
        self.label.move(50, 120)
        self.label.setWordWrap(True)

        self.label = QLabel('', self)
        self.label.move(50, 120)
        self.label.setWordWrap(True)

        self.r1.toggled.connect(self.radio_changed)

    def radio_changed(self):
        if self.r1.isChecked():
            self.label.setText('1st Variation')
        elif self.r2.isChecked():
            self.label.setText('2nd Variation')

        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())