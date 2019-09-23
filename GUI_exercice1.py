'''
Display an on-screen control consisting of QSlider and QLCDNumber.
Each updated value of the slider must display the updated value on the QLCDNumber display screen.
Values ​​range from 0 to 100.
Bonus: When the value is greater than 90, the entire screen must be painted green.
'''

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout)
from PyQt5.QtCore import Qt


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('Update number with Slider')
        self.lcd = QLCDNumber()
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.valueChanged.connect(self.update_numbers_in_slider)

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(slider)
        self.setLayout(layout)

    def update_numbers_in_slider(self, counter):
        #print(counter)
        self.lcd.display(counter)


app = QApplication(sys.argv)
animation = AppDemo()
animation.show()

app.exec_()
