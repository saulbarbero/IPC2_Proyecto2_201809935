from Cola import Cola # lista de robots | ciudades
from Matriz import Matriz #mapa de la ciudad

#objetos
from Ciudad import Ciudad 
from Robot import Robot
from Ciudad import unidadMapa


import xml.etree.ElementTree as ET


class Recurso:
    def __init__(self, robots, ciudades):
        self.robots = robots
        self.ciudades = ciudades


    def obtenerData(self, path):
        tree = ET.parse(path)
        root = tree.getroot()

        for element in root:
            if element.tag == 'listaCiudades':
                for c in element:
                    # capturar ciudades
                    ciudad = self.capturarCiudad(c)
                    self.ciudades.insertarCiudad(ciudad)
            else:
                for r in element:
                    # capturar robots
                    self.robots.insertarCiudad(self.capturaRobot(r))


    
    def capturarCiudad(self, root):
        mapa = Matriz()
        city = Ciudad()
        lEntradas = Cola()

        for ciudad in root:
            if ciudad.tag == 'nombre':
                city.nombre = ciudad.text
            elif ciudad.tag == 'fila':
                #inicializando la lista, si estas estan nulas.
                if ciudad.text.find('C') > 1 and city.lCivil == None:
                    city.lCivil = Cola()
                if ciudad.text.find('R') > 1 and city.lRecurso == None:
                    city.lRecurso = Cola()
                self.crearMatriz(int(ciudad.attrib["numero"]), 0,  ciudad.text, mapa ,lEntradas, city.lCivil, city.lRecurso)

            else: #debe de ser una unidad militar
                self.crearMatriz(int(ciudad.attrib["fila"]), int(ciudad.attrib["columna"]), None, mapa, None, None, None)


        # mapa.recorrerPorFilas()
        city.mapa = mapa
        city.lEntrada = lEntradas

        return city


    def crearMatriz(self, fila, columna,  text, mapa, lEntradas, lcivil, lrecurso):

        if(text == None):
            mapa.insertar(6, columna, fila)
            return

        iterador = 1
        text = text.replace('"', '')
        for c in text:
            # print(f'Fila:{fila} Columna: {iterador} Content: {c}')
            if c == "*":
                mapa.insertar(1, iterador + 1, fila)
            elif c == " ":
                mapa.insertar(2, iterador + 1, fila)
            elif c == "E":
                mapa.insertar(3, iterador + 1, fila)

                lEntradas.insertar(unidadMapa(iterador, fila, 0))
            elif c == "R":
                #agregar el elemento a una nueva lista
                lrecurso.insertar(unidadMapa(iterador, fila, 2))
                mapa.insertar(4, iterador + 1, fila)
            elif c == "C":
                #agrear el elemento a una nueva lista.
                lcivil.insertar(unidadMapa(iterador, fila, 1))
                mapa.insertar(5, iterador + 1, fila)
            iterador += 1





    def capturaRobot(self, root):
        root = root.find('nombre')
        robot = None
        if root.attrib["tipo"] == "ChapinFighter":
            robot = Robot(root.text, root.attrib["capacidad"], root.attrib["tipo"], 1)
        else:
            robot = Robot(root.text, -1, root.attrib["tipo"], 1)


        return robot






