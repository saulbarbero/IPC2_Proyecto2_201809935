

class ListaCabecera:
    def __init__(self):
        self.tam = 0
        self.primero = None
        self.ultimo = None

    def insertar(self, nuevo):
        self.tam += 1
        if(self.primero == None):
            self.primero = self.ultimo = nuevo
            #test
            self.primero.siguiente = self.ultimo
            self.ultimo.anterior = self.primero
            print('')
        else:
            if(nuevo.posicion < self.primero.posicion):
                nuevo.siguiente = self.primero
                nuevo.anterior = self.ultimo
                self.ultimo.siguiente = nuevo
                self.primero.anterior = nuevo
                self.primero = nuevo
            else:
                pivote = self.primero
                while(int(nuevo.posicion) >= int(pivote.posicion)):
                    if(int(nuevo.posicion) == int(pivote.posicion)):
                        return
                    if(pivote == self.ultimo):
                        self.ultimo.siguiente = nuevo
                        nuevo.anterior = self.ultimo
                        nuevo.siguiente = self.primero
                        self.primero.anterior = nuevo
                        self.ultimo = nuevo
                        return
                    pivote = pivote.siguiente

                pivote.anterior.siguiente = nuevo
                nuevo.anterior = pivote.anterior
                nuevo.siguiente = pivote
                pivote.anterior = nuevo

        print('')
    
    def obtenerNodoCabecera(self, posicion):
        if(self.primero == None):
            return None

        pivote = self.primero
        for i in range(self.tam):
            if( pivote.posicion == posicion):
                return pivote
            
            pivote = pivote.siguiente

        return None

    def recorrer(self):
        if(self.primero == None):
            print('Lista Vacia')

        pivote = self.primero
        for i in range(self.tam):
            print(pivote.posicion)
            
            pivote = pivote.siguiente


        

