# напиши тут код основної програми та першого екрану
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit

import second_win, final_win

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Здоров'я")
main_win.move(900, 70)
main_win.resize(1000, 600)
layout = QVBoxLayout()


class TestWin(QWidget):
    def __init__(self):
        super.__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()


main_win.show()
app.exec_()
