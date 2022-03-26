from Recurso import Recurso
from Cola import Cola #Esto realemte es una lista no una cola

from Ciudad import Ciudad
from Robot import Robot
robots = Cola()
ciudades = Cola()


menuPrincipal = {
    1: 'Cargar Archivo',
    2: 'Realizar Mision',
    3: 'Salir'
}

control = {
    1: 'Mision de Rescate',
    2: 'Mision de extraccion',
    3: 'Regresar'
}

def printMenu(menu):
    for i in range(1, len(menu) + 1):
        print(f'{i}-. {menu[i]}')

def menuP():
    
    
    while True:
        printMenu(menuPrincipal)

        entrada = input('Seleccione una opcion: ')
        entrada = int(entrada)

        if entrada == 1:
            path = input('Ingrese la ruta del archivo que desea cargar: ')
            recurso = Recurso(robots, ciudades)
            recurso.obtenerData(path)

        elif entrada == 2:
            while True:
                printMenu(control)
                inputControl = int(input('\nSeleccione una opcion valida: '))

                if inputControl == 1:
                    misionRescate()
                elif inputControl == 2:
                    misionExtraccion()
                else:
                    break

        else:
            return



def misionRescate():
    print('Mision rescate')
    ciudad = Ciudad()
    robot = Robot('','','')
    lRescate = ciudad.obtenerLCiviles(ciudades)
    lRobots = robot.obtenerlRobotsDisponibles(0, robots)
    if lRescate == None or lRobots == None:
        return

    #ejecutar mision, hay mas puntos de entrada ? solicitar el punto de entrada. 

    lRobots.recorrerLista(0)

    

def misionExtraccion():
    print('Mision Extraccion')




if __name__ == "__main__":
    menuP()

    print('Gracias por usar la app, cerdo.')
    exit()

