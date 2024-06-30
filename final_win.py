# напиши тут код третього екрана програми
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

app2 = QApplication([])
main_win2 = QWidget()
main_win2.setWindowTitle("Результати")
main_win2.move(900, 70)
main_win2.resize(1000, 600)
layout = QVBoxLayout()

index = 0
result = ""

text1 = QLabel(f"Індекс Рут'є: {index}")
text2 = QLabel(f"Працездатність серця: {result}")

layout.addWidget(text1, alignment=Qt.AlignCenter)
layout.addWidget(text2, alignment=Qt.AlignCenter)

main_win2.setLayout(layout)
