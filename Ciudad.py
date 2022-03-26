from Matriz import Matriz
from Cola import Cola

class Ciudad:
    def __init__(self, m = Matriz(), lEntrada = None, nombre = "default"):
        self.mapa = m
        self.recurso = 0
        self.civil = 0
        self.lEntrada = lEntrada
        self.nombre = nombre

    def obtenerLCiviles(self, lCiudad:Cola):
        if lCiudad.primero == None:
            print('La Lista de ciudades esta vacia.')
            return None

        
        lCiviles = Cola()
        pivote = lCiudad.primero
        while(pivote != None):

            if pivote.dato.civil > 0:
                lCiviles.insertar(pivote.dato)

            pivote = pivote.siguiente

        

        if lCiviles.tam > 0:
            return lCiviles
        
        return None

    def obtenerLRecurso(self, lCiudad:Cola):
        if lCiudad.primero == None:
            print('La lista de ciudades esta vacia')
            return None

        lRecursos = Cola()

        pivote = lCiudad.primero
        while(pivote != None):

            if pivote.dato.recurso > 0:
                lRecursos.insertar(pivote.dato)

            pivote = pivote.siguiente
        

        if lRecursos.tam > 0:
            return lRecursos

        return None

    def imprimir(self, tipo):
        if int(tipo) == 0:
            print(f'Ciudad: {self.nombre} Cant. Recursos: {self.recurso}')
        else:
            print(f'Ciudad: {self.nombre} Cant. Civiles: {self.civil}')