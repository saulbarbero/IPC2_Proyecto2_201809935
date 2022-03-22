from Matriz import Matriz

class Ciudad:
    def __init__(self, m = Matriz(), lEntrada = None, nombre = "default"):
        self.mapa = m
        self.recurso = False
        self.civil = False
        self.lEntrada = lEntrada
        self.nombre = nombre