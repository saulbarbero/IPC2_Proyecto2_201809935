from Recurso import Recurso
from Cola import Cola
robots = Cola()
ciudades = Cola()



if __name__ == "__main__":


    recurso = Recurso(robots, ciudades)



    recurso.obtenerData('Entrada_Ejemplo.xml')
    recurso.obtenerData('Entrada_Ejemplo.xml')
