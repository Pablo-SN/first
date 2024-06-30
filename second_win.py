# напиши тут код для другого екрана програми
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

app1 = QApplication([])
main_win1 = QWidget()
main_win1.setWindowTitle("Здоров'я")
main_win1.move(900, 70)
main_win1.resize(1000, 600)
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
main_layout = QHBoxLayout()

text1 = QLabel("Введіть П.І.Б.:")
PIB_input = QLineEdit("П.І.Б.")
text2 = QLabel("Пвних років:")
age_input = QLineEdit("0")
text3 = QLabel("Ляжте на спину і заміряйте пульс за 15с. Натисніть на копку 'Почати перший тест', щоб запустити "
               "таймер. \n Результат запишіть у відповідне поле.")
first_button = QPushButton("Почати перший тест")
first_pulse_input = QLineEdit("0")
text4 = QLabel("Виконайте 30 присідань за 45с. Для цього натисніть на кнопку 'Почати робити присідання', щоб запустити "
               "лічильник присідань.")
second_button = QPushButton("Почати робити присідання")
text5 = QLabel("Лягте на спину і заміряйте пульс спочатку за перші 15с хвилини, потім за останні 15с хвилини без виміру"
               " пульсацій. Результати запишіть у відповідні поля")
final_button = QPushButton("Почати фінальний тест")
second_pulse_input = QLineEdit("0")
final_pulse_input = QLineEdit("0")
next_button = QPushButton("Надіслати результати")
timer = QLabel()

layout1.addWidget(text1, alignment=Qt.AlignLeft)
layout1.addWidget(PIB_input, alignment=Qt.AlignLeft)
layout1.addWidget(text2, alignment=Qt.AlignLeft)
layout1.addWidget(age_input, alignment=Qt.AlignLeft)
layout1.addWidget(text3, alignment=Qt.AlignLeft)
layout1.addWidget(first_button, alignment=Qt.AlignLeft)
layout1.addWidget(first_pulse_input, alignment=Qt.AlignLeft)
layout1.addWidget(text4, alignment=Qt.AlignLeft)
layout1.addWidget(second_button, alignment=Qt.AlignLeft)
layout1.addWidget(text5, alignment=Qt.AlignLeft)
layout1.addWidget(first_button, alignment=Qt.AlignLeft)
layout1.addWidget(second_pulse_input, alignment=Qt.AlignLeft)
layout1.addWidget(final_pulse_input, alignment=Qt.AlignLeft)
layout1.addWidget(next_button, alignment=Qt.AlignCenter)
main_layout.addLayout(layout1)
main_win1.setLayout(main_layout)

