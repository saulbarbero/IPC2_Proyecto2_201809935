from Cola import Cola


class Robot:
    def __init__(self, nombre, capacidad, tipo , disponibilidad = -1):
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo
        self.disponibilidad = disponibilidad


    def obtenerlRobotsDisponibles(self, tipo, lista:Cola):
        
        
        if int(tipo) == 0:
            #rescue
            return self._obtenerlRobotsR(lista)
        else:
            #fighter
            return self.__obtenerlRobotsF(lista)


    def _obtenerlRobotsR(self, lista:Cola):
        if lista.primero == None:
            print('La lista de robots esta vacia x(')
            return None

        pivote = lista.primero
        lRescue = Cola()

        while(pivote != None):

            if pivote.dato.tipo == "ChapinRescue" and pivote.dato.disponibilidad > 0:
                lRescue.insertar(pivote.dato)
            pivote = pivote.siguiente

        if lRescue.tam > 0:
            return lRescue
        
        return None

    def __obtenerlRobotsF(self, lista:Cola):
        if lista.primero == None:
            print('La lista de robots esta vacia x(')
            return None

        pivote = lista.primero
        lRescue = Cola()

        while(pivote != None):

            if pivote.dato.tipo == "ChapinFighter" and pivote.dato.disponibilidad > 0:
                lRescue.insertar(pivote.dato)
            pivote = pivote.siguiente

        if lRescue.tam > 0:
            return lRescue
        
        return None


    def imprimir(self, tipo):
        print(f'Robot: {self.nombre} Disponible: {self.disponibilidad}')