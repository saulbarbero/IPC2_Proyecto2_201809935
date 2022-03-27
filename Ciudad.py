from Cola import Cola
from Matriz import Matriz


class Ciudad:
    def __init__(self, m = Matriz(), lEntrada = None, nombre = "default"):
        self.mapa = m
        self.lRecurso = None
        self.lCivil = None
        self.lEntrada = lEntrada
        self.nombre = nombre



    def obtenerLCiviles(self, lCiudad:Cola):
        if lCiudad.primero == None:
            print('La Lista de ciudades esta vacia.')
            return None

        
        lCiviles = Cola()
        pivote = lCiudad.primero
        while(pivote != None):

            if pivote.dato.lCivil != None:
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

            if pivote.dato.lRecurso != None:
                lRecursos.insertar(pivote.dato)

            pivote = pivote.siguiente
        

        if lRecursos.tam > 0:
            return lRecursos

        return None

    def imprimir(self, tipo):
        if int(tipo) == 0:
            print(f'Ciudad: {self.nombre} Cant. Recursos: {self.lRecurso.tam}')
        else:
            print(f'Ciudad: {self.nombre} Cant. Civiles: {self.lCivil.tam}')


class unidadMapa:
    def __init__(self, x=0, y=0, tipo=-1):
        self.x = x
        self.y = y
        self.tipo = tipo

    def imprimir(self, tipo):
        if int(tipo) == 0:
            print(f'Entrada en coordenadas x,y: {self.x},{self.y}')
        elif int(tipo) == 1:
            print(f'Unidad Civil en coordenadas x,y: {self.x},{self.y}')
        else:
            print(f'Recurso en coordenadas x,y: {self.x},{self.y}')

