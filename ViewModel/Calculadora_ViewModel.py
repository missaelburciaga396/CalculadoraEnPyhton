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
        self.display_changed.emit(self._expression)

    def boton_clear(self):
        self._expression = ""
        self.display_changed.emit(self._expression)

    def obtener_resultado(self):
        resultado = self._model.getResultado(self._expression)
        self.display_changed.emit(resultado)
        self._expression = resultado if resultado != "Error" else ""