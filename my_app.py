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


def next_page():
    app.closeAllWindows()
    second_win.main_win1.show()
    second_win.app1.exec_()


def last_page():
    second_win.app1.closeAllWindows()
    final_win.main_win2.show()
    final_win.app2.exec_()
    second_win.main_win1.show()
    second_win.app1.exec_()


text1 = QLabel("Ласкаво просимо до програми визначення стану здоров'я!")
text2 = QLabel("Ця програма дозволить вам за допомогою тесту Руф'є провести первинну діагностику вашого здоров'я. \n"
               "Проба Руф'є є навантажувальним комплексом, призначеним для оцінки працездатності серця при фізичному "
               "навантаженні. \n У випробуваного, що знаходиться в положенні лежачи на спині протягом 5хв, визначають "
               "частоту пульсу за 15с; \n потім протягом 45с випробуваний виконує 30 присідань. \n Після закінчення "
               "Навантаження випробуваний лягає, і в нього знову підраховується кількість пульсацій за перші 15с, \n"
               "Важливо! Якщо в процесі проведення випробовування ви відчуваєте себе погано(з'явиться запаморочення, "
               "шум \n у вухах, сильна задишка та ін.), то тест необхідно перервати і звернутися до лікаря.")
button = QPushButton("Почати")
button.pressed.connect(next_page)
second_win.next_button.pressed.connect(last_page)
layout.addWidget(text1, alignment=Qt.AlignLeft)
layout.addWidget(text2, alignment=Qt.AlignLeft)
layout.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(layout)
main_win.show()
app.exec_()
