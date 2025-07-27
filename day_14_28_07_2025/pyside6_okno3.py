import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QLabel, QPushButton, QStyleFactory
)

# funkcja uruchamiana po nacisnieciu buttona
def show_text():
    label.setText(textbox.text())

app = QApplication(sys.argv)

print(QStyleFactory.keys())  # ['macOS', 'Windows', 'Fusion']
app.setStyle("macOS")
# app.setStyle("Fusion")

dialog = QWidget()
dialog.setWindowTitle("Okno z polem tekstowym")
dialog.setGeometry(100, 100, 300, 150)

# pole tekstowe
textbox = QLineEdit()
textbox.setPlaceholderText("Wpisz coś tutaj...")

# labelka
label = QLabel("Tekst pojawi się tutaj")

# button
button = QPushButton("Wyświetl tekst")

# podłaczenie przycisku z funkcją
button.clicked.connect(show_text)

# podłaczenie Entera z polem tekstowym
textbox.returnPressed.connect(show_text)

# budujemy Layout
layout = QVBoxLayout()

layout.addWidget(textbox)
layout.addWidget(button)
layout.addWidget(label)

dialog.setLayout(layout)

dialog.show()
sys.exit(app.exec())
