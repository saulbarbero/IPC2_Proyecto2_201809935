from ListaCabecera import ListaCabecera
from NodoOrtogonal import NodoOrtogonal
from NodoCabecera import NodoCabecera
from Cola import Cola
from os import system

class Matriz:
    def __init__(self, pa = ""):
        self.filas = ListaCabecera()
        self.columnas = ListaCabecera()
        self.patronA = pa



    def deleteReferences(self):
        efila = self.filas.primero
        for i in range(self.filas.tam):
            actual = efila.acceso
            while (actual != None):

                if actual.isPath == True:
                    # print(f'Borrando isPath: {actual.x},{actual.y}')
                    actual.isPath = False

                if actual.visited == True:
                    # print(f'Borrando visited: {actual.x},{actual.y}')
                    actual.visited = False

                actual = actual.dcho
            efila = efila.siguiente


        return self

    def insertar(self, valor, x, y, militar): # 4x3 -> wwbbbwwwwb -> x, y
        nuevo = NodoOrtogonal(x, y, valor, militar)

        fila = self.filas.obtenerNodoCabecera(y)
        self.insertarFilas(nuevo, fila)

        columna = self.columnas.obtenerNodoCabecera(x)
        self.insertarColumnas(nuevo, columna)

    #probar esto
    def insertarFilas(self, nuevo : NodoOrtogonal, fila: NodoCabecera):
        if( fila == None ):
            fila = NodoCabecera(nuevo.y)
            self.filas.insertar(fila)
            fila.acceso = nuevo
        else:
            if(nuevo.x < fila.acceso.x): # insertar al inicio
               nuevo.dcho = fila.acceso
               fila.acceso.izdo = nuevo
               fila.acceso = nuevo
            else:
                pivote = fila.acceso
                while(nuevo.x >= pivote.x):
                    if nuevo.x == pivote.x:
                        # pivote = nuevo
                        pivote.dato = nuevo.dato
                        pivote.militar = nuevo.militar
                        return
                    if pivote.dcho == None:
                        pivote.dcho = nuevo
                        nuevo.izdo = pivote
                        return
                    pivote = pivote.dcho
                pivote.izdo.dcho = nuevo # nodo intermedio
                nuevo.izdo = pivote.izdo
                nuevo.dcho = pivote
                pivote.izdo = nuevo 

    def insertarColumnas(self, nuevo: NodoOrtogonal, columna: NodoCabecera):
        if columna == None:
            columna = NodoCabecera(nuevo.x)
            self.columnas.insertar(columna)
            columna.acceso = nuevo
        else:
            pivote = columna.acceso
            while(nuevo.y >= pivote.y):
                if nuevo.y == pivote.y:
                    #sobre-escribir el valor de ese punto.
                    pivote.dato = nuevo.dato
                    pivote.militar = nuevo.militar
                    # pivote = nuevo
                    return
                if pivote.abjo == None:
                    pivote.abjo = nuevo
                    nuevo.arrb = pivote
                    return
                pivote = pivote.abjo
            
            pivote.arrb.abjo = nuevo
            nuevo.arrb = pivote.arrb
            nuevo.abjo = pivote
            pivote.arrb = nuevo


    def recorrerPorFilas(self):
        efila = self.filas.primero
        for i in range(self.filas.tam):
            actual = efila.acceso
            print('Fila#: ' +  str(efila.posicion))
            while(actual != None):
                salida = str(actual.dato) + " x:"  + str(actual.x) + " y:" + str(actual.y) + " path:" + str(actual.isPath)
                print(salida)

                actual = actual.dcho
            efila = efila.siguiente


                # poder generar diferentes matrices.
    def graficarMatriz(self, nombre):
        miArchivo = open(nombre + '.dot','w')
        miArchivo.write(self.__graphPix())
        miArchivo.close()

        arg = 'dot -Tpng ' +  nombre + '.dot -o ' + nombre + '.png'
        system(arg)
        # system('cd ./' + nombre + '.png')
        # startfile(nombre + '.png')

    def __graphPix(self):
        buffer = ""
        buffer += "digraph matriz{\n"
        buffer += "graph[nodesep=0.02, ranksep=0.0005, margin=0.05, ratio=\"compress\"];\n"
        buffer += "node[shape=box, style=filled];\n"
        buffer += "edge[color=white dir=none];\n"
        buffer += "rankdir=UD;\n"

        buffer += self.__cabeceraYP()
        buffer += '\n'

        buffer += self.__dotEnlaceX()
        buffer += '\n'

        buffer += self.__dotEnlaceY()
        buffer += '\n'

        buffer += '}'

        return buffer

    def __cabeceraYP(self):
        buffer = ""
        efila = self.filas.primero

        while True:
            if(efila != None):
                buffer += "{rank=same;"
                actual = efila.acceso
                while actual != None:
                    buffer += "\"xy:" + str(actual.x) + "," + str(actual.y) + "\""
                    buffer += "[label=\"" + str(actual.x) + "," + str(actual.y)
                    buffer += "\",style=filled fillcolor=" + self.__obtenerColor(actual)
                    buffer += "];"

                    actual = actual.dcho

                buffer += "}\n"

            efila = efila.siguiente
            if efila == self.filas.primero:
                break
        return buffer
    
    def __dotEnlaceX(self):
        buffer = ""
        actual = None
        ecolumna = self.columnas.primero
        while True:
            
            if ecolumna != None:
                if ecolumna.acceso == None:
                    ecoluma = ecolumna.siguiente
                    continue
                
                actual = ecolumna.acceso
                while actual != None:
                    if actual.abjo != None:
                        buffer += "\"xy:" + str(actual.x) + "," + str(actual.y) + "\""
                        buffer += "->"
                        buffer += "\"xy:" + str(actual.abjo.x) + "," + str(actual.abjo.y) + "\""
                        buffer += ";\n"
                    else:
                        break
                    actual = actual.abjo

            ecolumna = ecolumna.siguiente
            if ecolumna == self.columnas.primero:
                break


        return buffer

    def __dotEnlaceY(self):
        buffer = ""
        actual = None
        efila = self.filas.primero
        while True:
            if efila != None:
                if efila.acceso == None:
                    efila = efila.siguiente
                    continue

                actual = efila.acceso
                while actual != None:

                    if actual.dcho == None:
                        break

                    buffer += "\"xy:" + str(actual.x) + "," + str(actual.y) + "\""
                    if actual.dcho != None:
                        buffer += "->"
                        buffer += "\"xy:" + str(actual.dcho.x) + "," + str(actual.dcho.y) + "\""
                        buffer += "[constraint=false];\n"

                    actual = actual.dcho

            efila = efila.siguiente
            if efila == self.filas.primero:
                break

        return buffer



    def flip(self, valor):
        if valor == "W":
            return "B"
        
        return "W"

    def buscarNodo(self, x, y, m):
        efila = m.filas.obtenerNodoCabecera(y)
        if efila == None:
            return None

        pivote = efila.acceso
        while pivote != None:
            if int(pivote.x) == int(x):
                return pivote

            pivote = pivote.dcho


        return None

    def buscarPorPosicion(self, x, y):
        efila = self.filas.obtenerNodoCabecera(y)

        if efila == None:
            return None

        pivote = efila.acceso
        while(pivote != None):
            if int(pivote.x) == int(x):
                return pivote


            pivote = pivote.dcho

        return None


    def __obtenerColor(self, actual):

        if actual.isPath == True:
            return "darkolivegreen"

        if actual.dato == 1:
            return 'black'
        elif actual.dato == 2:
            return 'white'
        elif actual.dato == 3:
            return 'green'
        elif actual.dato == 4:
            return 'gray'
        elif actual.dato == 5:
            return 'blue'
        elif actual.dato == 6:
            return 'red'
        # return actual.dato # los colres correctamente

    
