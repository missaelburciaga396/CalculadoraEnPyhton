import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from ViewModel.Calculadora_ViewModel import CalculadoraViewModel


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self._viewModel = CalculadoraViewModel()
        self.setWindowTitle("Calculadora V2")
        self.setGeometry(100, 100, 300, 350)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        #display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        self.display.setStyleSheet("font-size: 18px;")
        #agregar display
        self.layout.addWidget(self.display)
        self._viewModel.display_changed.connect(self.display.setText)

        #agregar botones
        buttons = [
            "1","2","3","/",
            "4","5","6","*",
            "7","8","9","+",
            "0",".","C","-",
            "="
        ]

        row, col = 0,0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(50, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db; 
                    color: white;              
                    font-size: 16px;            
                    border-radius: 10px;        
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)

            self.grid_layout.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1
            #agregar las funciones a los botones
            if button == "C":
                btn.clicked.connect(self._viewModel.boton_clear)
            elif button == "=":
                btn.clicked.connect(self._viewModel.obtener_resultado)
            else:
                btn.clicked.connect(lambda checked, b=button: self._viewModel.agregar_expresion(b))
        self.layout.addLayout(self.grid_layout)

        self.widget.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = MainView()
    MainWindow.show()

    sys.exit(app.exec())
