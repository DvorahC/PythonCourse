import sys
from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *

'''
COLOR BOX
Display a control that includes two QLabel and one QPushButton button.
In one box should be written "Color Is:",
pressing the button should open a dialog for selecting color and in the other box the name of the selected color should be written.

The dialog can be displayed using the QColorDialog : getColor function.
After receiving the color, the QColor : name function returns its name.
'''

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 color Box'
        self.value = None
        self.left = 10
        self.top = 100
        self.width = 400
        self.height = 200
        self.MainUI()

    def MainUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('Open color dialog', self)
        color_answer = QLabel(self.text())
        button.move(10, 10)
        color_answer.move(60, 60)
        button.clicked.connect(self.on_click)
        button.clicked.connect(self.open_color_dialog)

        self.show()

    def on_click(self):
        self.open_color_dialog()

    def open_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.value = color.name()
            self.text()
            print(self.value)

    def text(self):
        return f'The color is: {self.value}'


app = QApplication(sys.argv)
w = App()
w.show()

app.exec_()

