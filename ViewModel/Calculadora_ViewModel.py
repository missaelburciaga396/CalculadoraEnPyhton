from PySide6.QtCore import QObject, Signal
from Model.Calculadora_Model import CalculadoraModel
class CalculadoraViewModel(QObject):

    display_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self._expression = ""
        self._model = CalculadoraModel

    def agregar_expresion(self, value):
        self._expression += value
        self.lista_de_operadores = ["+", "-", "/" ]
        if self._expression.count("*") > 2:
            self._expression ="Error"
        for i in self.lista_de_operadores:
            if self._expression.count(i) > 1:
                self._expression = "Error"

        if self._expression[:-1] == "Error" and len(self._expression) > 5:
            self._expression =""

        self.display_changed.emit(self._expression)

    def boton_clear(self):
        self._expression = ""
        self.display_changed.emit(self._expression)

    def obtener_resultado(self):
        resultado = self._model.getResultado(self._expression)
        self.display_changed.emit(resultado)
        self._expression = resultado if resultado != "Error" else ""

    def eliminarUltimaExpresion(self):
        self._expression = self._expression[:-1]
        self.display_changed.emit(self._expression)