# напиши тут код для другого екрана програми
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from instr import *
from final_win import FinalWin


class Experiment:
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.test1 = int(test1)
        self.test2 = int(test2)
        self.test3 = int(test3)


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.connects()  # Встановлює зв'язки між елементами
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.text1 = QLabel(txt_name)
        self.PIB_input = QLineEdit(txt_hintname)
        self.text2 = QLabel(txt_age)
        self.age_input = QLineEdit(txt_hintage)
        self.text3 = QLabel(txt_test1)
        self.first_button = QPushButton(txt_starttest1)
        self.first_pulse_input = QLineEdit(txt_hinttest1)
        self.text4 = QLabel(txt_test2)
        self.second_button = QPushButton(txt_starttest2)
        self.text5 = QLabel(txt_test3)
        self.final_button = QPushButton(txt_starttest3)
        self.second_pulse_input = QLineEdit(txt_hinttest2)
        self.final_pulse_input = QLineEdit(txt_hinttest3)
        self.next_button = QPushButton(txt_sendresults)
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()

        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()

        self.l_line.addWidget(self.text1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.PIB_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.first_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.first_pulse_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text4, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.second_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text5, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.final_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.first_button, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.second_pulse_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.final_pulse_input, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.next_button, alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.time, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
        self.hide()
        self.exp = Experiment(self.age_input.text(), self.first_pulse_input.text(), self.second_pulse_input.text(),
                              self.final_pulse_input.text())
        self.fw = FinalWin(self.exp)

    def connects(self):
        self.next_button.clicked.connect(self.next_click)
