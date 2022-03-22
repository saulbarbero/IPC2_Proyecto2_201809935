from os import system


class Nodo:
  def __init__(self, dato = None):
    self.dato = dato
    self.siguiente = None
    self.anterior = None


class Cola:
    def __init__(self):
      self.primero = None
      self.ultimo = None
      self.tam = 0


    def insertarCiudad(self, dato):
        if self.buscarDato(dato):
            return

        self.insertar(dato)

    def buscarDato(self, dato):
        if self.primero == None:
            return False


        pivote = self.primero
        while(pivote != None):
            if(pivote.dato.nombre == dato.nombre): #podria dar problema
                return True

            pivote = pivote.siguiente

        return False

    def insertar(self, dato):
        self.tam += 1
        nuevo = Nodo(dato = dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def dequeue(self):
        
        if self.tam == 1:
            self.primero = self.ultimo = None
            return

        aux = self.primero.siguiente
        aux.anterior = None
        self.primero.siguiente = None
        self.primero = aux

        self.tam -= 1


        print(f'Eliminado Orden#: {aux.dato.id}')

        return aux


    def recorrerLista(self):
        if(self.primero == None):
            return

        pivote = self.primero
        while(pivote != None):
            print(pivote.dato)
            pivote = pivote.siguiente


    def generarReporte(self, nombre):
        if self.primero == None:
            print('Cola Vacia ')
            return

        buffer = "digraph G{node[shape=record];\nrankdir=LR;"
        buffer += self.generarDot()
        buffer += "\n}"

        miArchivo = open(nombre + '.dot','w')
        miArchivo.write(buffer)
        miArchivo.close()

        arg = 'dot -Tpng ' +  nombre + '.dot -o ' + nombre + '.png'
        system(arg)
        # system('cd ./' + nombre + '.png')
        # startfile(nombre + '.png')



    def generarDot(self):
        buffer = ""

        if self.primero == None:
            return ""

        pivote = self.primero

        while(pivote != None):

            buffer += "node" + str(hash(pivote))
            buffer += f'[label="Orden# {pivote.dato.id}\\nCliente:{pivote.dato.nombre}\\nCantidad de Pizzas:{pivote.dato.pizza.tam}\\nTiempo de la Orden:{pivote.dato.tiempo}"];\n'

            if pivote.siguiente != None:
                buffer += "node" + str(hash(pivote.siguiente))
                buffer += f'[label="Nombre Cliente:{pivote.siguiente.dato.nombre}\\nCantidad de Pizzas:{pivote.siguiente.dato.pizza.tam}\\nTiempo de la Orden:{pivote.siguiente.dato.tiempo}"];\n'

                buffer += "node" + str(hash(pivote))
                buffer += "->"
                buffer += "node" + str(hash(pivote.siguiente)) + "\n"

            pivote = pivote.siguiente


        return buffer


#definir aqui el objeto.