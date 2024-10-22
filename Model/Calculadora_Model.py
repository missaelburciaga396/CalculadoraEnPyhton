class CalculadoraModel:
    @staticmethod
    def getResultado(finalvalor):
        try:
            valor = eval(finalvalor)
            return str(valor)
        except Exception:
            return "Error"