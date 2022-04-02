class NodoOrtogonal:
    def __init__(self, x, y, dato):
        self.x = x
        self.y = y
        self.dato = dato
        self.arrb = None
        self.abjo = None
        self.izdo = None
        self.dcho = None
        self.visited = False #Se utilizara para saber si ya fue visitado durante el algoritmo de busqueda de la ruta.
        self.isPath = False #Este me indicara, si este nodo es parte de la ruta trazada para llegar al punto destino.
        

