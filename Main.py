import sys
from PySide6.QtWidgets import QApplication
from View.CalculadoraMain_View import MainView




if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = MainView()
    MainWindow.show()

    sys.exit(app.exec())