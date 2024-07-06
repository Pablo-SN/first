# напиши тут код основної програми та першого екрану
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

from second_win import TestWin

app = QApplication([])


win2 = TestWin()
win2.set_appear()
win2.initUI()
win2.show()

app.exec_()
