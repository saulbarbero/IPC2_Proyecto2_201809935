from Recurso import Recurso
from Cola import Cola
from  Recurso  import Recurso
from Ciudad import Ciudad
from Robot import Robot
from pdf import generarPDF 
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
    print('**Mision rescate**')
    ciudad = Ciudad()
    robot = Robot('','','')

    lRescate = ciudad.obtenerLCiviles(ciudades)
    lRobots = robot.obtenerlRobotsDisponibles(0, robots)
    civil = None
    entrada = None

    if lRescate == None or lRobots == None:
        print('Error: No se encuentran unidades Civiles en la ciudad seleccionada')
        return

    #Seleccionando la Ciudad

    print('**Segun inteligencia, este es el listado de ciudades que contienen Civiles**')

    while True:
        lRescate.recorrerLista(1)
        entradaCiudad = int(input('Seleccione una Ciudad para desplegar la mision: '))
        ciudad = lRescate.buscarPorPosicion(entradaCiudad)

        if ciudad != None:
            break

    #Seleccionando el Robot
    if lRobots.tam > 1: # nos indica que hay mas de un robot, se debe de poder elegir el robot deseado
        while True:
            lRobots.recorrerLista(-1)
            entradaRobot = int(input('Seleccione un Robot para la misión: '))
            robot = lRobots.buscarPorPosicion(entradaRobot)

            if robot != None:
                break

    else:
        robot = lRobots.primero.dato


    #Seleccionando la unidad civil

    if ciudad.lCivil.tam > 1:
        while True:
            ciudad.lCivil.recorrerLista(1)
            entradaCivil = int(input('Seleccione una unidad civil a rescatar: '))
            civil = ciudad.lCivil.buscarPorPosicion(entradaCivil)

            if civil != None:
                break

    else:
        civil = ciudad.lCivil.primero.dato


    #Seleccionando la Entrada
    if ciudad.lEntrada.tam > 1:
        while True:
            ciudad.lEntrada.recorrerLista(0)
            entradaE = int(input('Selecciona una entrada para la mision: '))
            entrada = ciudad.lEntrada.buscarPorPosicion(entradaE)

            if entrada != None:
                break
    else:
        entrada = ciudad.lEntrada.primero.dato



    # tenemos la entrada, la ciudad, el robot y la unidad civil

    print(f'La mision de rescate se ejecutara en la ciudad: {ciudad.nombre}')
    print(f'La Ejecutara el Robot: {robot.nombre}')
    print(f'Entrada a la ciudad en la coordenada: {entrada.x},{entrada.y} y Rescatara a una unidad Civil en: {civil.x},{civil.y}')
    print('########################################')


    ciudad.mapa.graficarMatriz(ciudad.nombre)
    ciudad.mapa.isPath(entrada.x, entrada.y, civil.x, civil.y)
    ciudad.mapa.graficarMatriz('salida')
    generarPDF("Mision de Rescate","salida","Mision de Rescate",robot.nombre)




    

def misionExtraccion():
    print('Mision Extraccion')
    ciudad = Ciudad()
    robot = Robot('', '', '')
    lRecursos = ciudad.obtenerLRecurso(ciudades)
    lRobots = robot.obtenerlRobotsDisponibles(1, robots)
    recurso = None
    entrada = None

    if lRecursos == None or lRobots == None:
        print('Error: No se encuentran unidades Civiles en la ciudad seleccionada')
        return

    print('**Segun inteligencia, este es el listado de ciudades que contienen Recursos Valiosos para nuestra operacion**')

    while True:
        lRecursos.recorrerLista(0)
        entradaCiudad = int(input('Seleccione una Ciudad para desplegar la mision: '))
        ciudad = lRecursos.buscarPorPosicion(entradaCiudad)

        if ciudad != None:
            break


    ## all
    # Seleccionando el Robot
    if lRobots.tam > 1:  # nos indica que hay mas de un robot, se debe de poder elegir el robot deseado
        while True:
            lRobots.recorrerLista(-1)
            entradaRobot = int(input('Seleccione un Robot para la misión: '))
            robot = lRobots.buscarPorPosicion(entradaRobot)

            if robot != None:
                break

    else:
        robot = lRobots.primero.dato

        # Seleccionando el Recurso

    if ciudad.lRecurso.tam > 1:
        while True:
            ciudad.lRecurso.recorrerLista(2)
            entradaCivil = int(input('Seleccione el recurso a recuperar: '))
            recurso = ciudad.lRecurso.buscarPorPosicion(entradaCivil)

            if recurso != None:
                break

    else:
        recurso = ciudad.lRecurso.primero.dato


    #as
        # Seleccionando la Entrada
    if ciudad.lEntrada.tam > 1:
        while True:
            ciudad.lEntrada.recorrerLista(0)
            entradaE = int(input('Selecciona una entrada para la mision: '))
            entrada = ciudad.lEntrada.buscarPorPosicion(entradaE)

            if entrada != None:
                break
    else:
        entrada = ciudad.lEntrada.primero.dato

    print(f'La mision de rescate se ejecutara en la ciudad: {ciudad.nombre}')
    print(f'La Ejecutara el Robot: {robot.nombre}')
    print(f'Entrada a la ciudad en la coordenada: {entrada.x},{entrada.y} y recuperara el Recurso en: {recurso.x},{recurso.y}')
    print('########################################')



if __name__ == "__main__":
    generarPDF("nombre","salida","mision","robot")
    menuP()

    print('Gracias por usar la app')
    exit()
