import sys
from PySide6.QtWidgets import QApplication, QWidget, QStyleFactory

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # wypisanie dostępnych styli
    print("Styles available:", QStyleFactory.keys())
    # Styles available: ['macOS', 'Windows', 'Fusion']

    app.setStyle(QStyleFactory.create("Fusion"))

    window = QWidget()
    window.setWindowTitle("Demo z Fusion")
    window.resize(300, 200)
    window.show()

    sys.exit(app.exec())
