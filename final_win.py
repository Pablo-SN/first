# напиши тут код третього екрана програми
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.show()
        self.lv = 0

    def result(self):
        self.lv = round((4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 10, 2)
        if self.exp.age >= 15:
            if self.lv >= 15:
                return txt_res1
            elif 11 <= self.lv <= 14.9:
                return txt_res2
            elif 6 <= self.lv <= 10.9:
                return txt_res3
            elif 0.5 <= self.lv <= 5.9:
                return txt_res4
            else:
                return txt_res5

        elif 13 <= self.exp.age <= 14:
            if self.lv >= 16.5:
                return txt_res1
            elif 12.5 <= self.lv <= 16.4:
                return txt_res2
            elif 7.5 <= self.lv <= 12.4:
                return txt_res3
            elif 2 <= self.lv <= 7.4:
                return txt_res4
            else:
                return txt_res5

        elif 11 <= self.exp.age <= 12:
            if self.lv >= 18:
                return txt_res1
            elif 14 <= self.lv <= 17.9:
                return txt_res2
            elif 9 <= self.lv <= 13.9:
                return txt_res3
            elif 3.5 <= self.lv <= 8.9:
                return txt_res4
            else:
                return txt_res5

        elif 9 <= self.exp.age <= 10:
            if self.lv >= 19.5:
                return txt_res1
            elif 15.5 <= self.lv <= 19.4:
                return txt_res2
            elif 10.5 <= self.lv <= 15.4:
                return txt_res3
            elif 5 <= self.lv <= 10.4:
                return txt_res4
            else:
                return txt_res5

        elif 7 <= self.exp.age <= 8:
            if self.lv >= 21:
                return txt_res1
            elif 17 <= self.lv <= 20.9:
                return txt_res2
            elif 12 <= self.lv <= 16.9:
                return txt_res3
            elif 6.5 <= self.lv <= 11.9:
                return txt_res4
            else:
                return txt_res5

        else:
            return txt_no_res

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.result()
        self.index_text = QLabel(txt_index + self.result())
        self.workh_text = QLabel(txt_workheart + str(self.lv))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
