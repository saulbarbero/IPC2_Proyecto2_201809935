from Cola import Cola
from NodoOrtogonal import NodoOrtogonal


class BusquedaRuta:
    def __init__(self, map, x, y, robot =None):
        self.matriz = map
        self.stack = Cola()
        self.xEnd = x
        self.yEnd = y
        self.robot = robot

    # def buscar(self, xStart, yStart):
    #     start = self.matriz.buscarPorPosicion(xStart, yStart)
    #     if not start:
    #         print('no se encontro la entrada')
    #         return
    #
    #     # self.Grafo = Grafo(start)
    #
    #     self.buscarRuta(self.Grafo, start)
    #
    # def buscarRuta(self, root: Grafo, parent: NodoOrtogonal):
    #
    #     root.dato.visited = True
    #
    #     if int(root.dato.x) == self.xEnd and int(root.dato.y) == self.yEnd:
    #         print('se ha encontrado la ruta')
    #         root.dato.visited = False
    #         root.dato.isPath = True # lo marco como ruta y propago ese valor hacia arriba
    #         return
    #
    #
    #
    #     self.explorarAdyancentes(root.dato.arrb, parent)
    #     self.explorarAdyancentes(root.dato.dcho, parent)
    #     self.explorarAdyancentes(root.dato.abjo, parent)
    #     self.explorarAdyancentes(root.dato.izdo, parent)
    #
    #
    #     if self.stack.tam < 1:
    #         print('pila vacia')
    #         return
    #
    #
    #     root.hijos.insertar(Grafo(self.stack.pop()))
    #     self.buscarRuta(root.hijos.ultimo.dato, root.dato)
    #
    #     # es cuando la pila no tenga datos.
    #
    # def explorarAdyancentes(self, actual: NodoOrtogonal, parent: NodoOrtogonal):
    #     if actual == None or actual.visited or actual == parent:
    #         return
    #
    #     # validar que no haya sido visitado. y no agregar al padre.
    #
    #     if actual.dato == 2 or actual.dato == 3 or actual.dato == 5:
    #         self.stack.insertar(actual)

    #--------------------------------------------------------------------------


    def isInsideMatrix(self, x, y):
        if x >= 0 and x <= self.matriz.columnas.tam and y >= 0 and y <= self.matriz.filas.tam:
            return True
        return False

    def isPath(self, xi, yi):

        lPath = Cola()
        flag = self._isPath(xi, yi, self.xEnd, self.yEnd, lPath, 1)

        pivote = lPath.primero
        while (pivote != None):
            pivote.dato.isPath = True

            pivote = pivote.siguiente

        if flag:
            print('Se encontrol la unidad deseada')
            return True
        else:
            print('No se encontro la unidad')
            return False


    def rescate(self, xi, yi):
        lPath = Cola()
        flag = self._isPath(xi, yi, self.xEnd, self.yEnd, lPath, 2)

        pivote = lPath.primero
        while (pivote != None):
            pivote.dato.isPath = True

            pivote = pivote.siguiente

        if flag:
            print('Se encontrol la unidad deseada')
            return True
        else:
            print('No se encontro la unidad')
            return False

    def validarNodo(self, nodo, tipo):
        if int(tipo) == 1:  # unidad civil
            if (int(nodo.dato) == 2 or int(nodo.dato) == 3 or int(nodo.dato) == 5) and nodo.visited == False:
                return True

        else:
            # unidad militar
            if int(nodo.dato) != 1 and nodo.visited == False:
                if int(nodo.dato) == 6:
                    if int(self.robot.capacidad) >= int(nodo.militar):
                        temp = int(self.robot.capacidad) - int(nodo.militar)
                        self.robot.capacidad = temp
                        # self.robot.capacidad -= int(nodo.militar)
                        nodo.militar = 0  # funcione, que si guarde la referencia en la matriz.
                        # nodo.dato = 1
                        return True
                    else:
                        print(f'La unidad militar no es lo suficientemente fuerte para luchar')
                        return False
                    # validar que la capacidad de pelea sea >= que la del nodo actual.


                return True

        return False

    def _isPath(self, x, y, xd, yd, l, tipo):
        nodo = self.matriz.buscarPorPosicion(x, y)

        if nodo == None:
            return False

        if self.validarNodo(nodo, tipo):
            nodo.visited = True
            l.insertar(nodo)

            if int(nodo.x) == int(xd) and int(nodo.y) == int(yd):
                print('Se encontro la ruta.')
                # nodo.dato = 2
                return True

            yr = yd - y  # 1
            xr = xd - x  # 10

            #yr > 1 debo ir hacia abajo
            #yr < 1 debo ir hacia arriba
            #yr  == 0 -> priorizar el movimiento en las columnas.

            if xr < 1:
                left = self._isPath(x - 1, y, xd, yd, l, tipo)

                if left:
                    return True

                rigth = self._isPath(x + 1, y, xd, yd, l, tipo)

                if rigth:
                    return True

            else:
                rigth = self._isPath(x + 1, y, xd, yd, l, tipo)

                if rigth:
                    return True

                left = self._isPath(x - 1, y, xd, yd, l, tipo)

                if left:
                    return True

            if yr < 1:
                up = self._isPath(x, y - 1, xd, yd, l, tipo)

                if up:
                    return True

                down = self._isPath(x, y + 1, xd, yd, l, tipo)

                if down:
                    return True

            else:
                down = self._isPath(x, y + 1, xd, yd, l, tipo)

                if down:
                    return True

                up = self._isPath(x, y - 1, xd, yd, l, tipo)

                if up:
                    return True

        # aqui buscar ese nodo dentro de la lista y removerlo.
        l.removerElemento(nodo)
        return False