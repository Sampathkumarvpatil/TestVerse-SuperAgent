import sys
from PySide6.QtWidgets import QApplication
from main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Testverse Superagent")
    w = MainWindow()
    w.setWindowTitle("Testverse Superagent")
    w.show()
    sys.exit(app.exec())
