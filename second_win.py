# напиши тут код для другого екрана програми
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *

second_win = QWidget()

text1 = QLabel(txt_name)
PIB_input = QLineEdit(txt_hintname)
text2 = QLabel(txt_age)
age_input = QLineEdit(txt_hintage)
text3 = QLabel(txt_test1)
first_button = QPushButton(txt_starttest1)
first_pulse_input = QLineEdit(txt_hinttest1)
text4 = QLabel(txt_test2)
second_button = QPushButton(txt_starttest2)
text5 = QLabel(txt_test3)
final_button = QPushButton(txt_starttest3)
second_pulse_input = QLineEdit(txt_hinttest2)
final_pulse_input = QLineEdit(txt_hinttest3)
next_button = QPushButton(txt_sendresults)
timer = QLabel(txt_timer)


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        second_win.setWindowTitle("Здоров'я")
        second_win.move(900, 70)
        second_win.resize(1000, 600)


    def show(self):
        second_win.show()

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.l_line.addWidget(second_win.text1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.PIB_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.text2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.age_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.text3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.first_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.first_pulse_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.text4, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.second_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.text5, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.first_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.second_pulse_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.final_pulse_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(second_win.next_button, alignment=Qt.AlignCenter)
        self.r_line.addWidget(second_win.timer, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        second_win.setLayout(self.h_line)
