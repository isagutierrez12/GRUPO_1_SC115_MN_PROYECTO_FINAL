'''
Radiador Springs S.A.

1. Ver rutas: En este apartado deben mostrarse al menos 5 rutas en las que
operará el servicio. Para efectos de este apartado puede crear un arreglo
unidimensional que almacene las cinco rutas en el formato: “Coronado – San José”. Entre otras.

2. Ver precios: En este apartado debe mostrarse al menos 3 opciones de
compra de tiquetes. Por ejemplo, “Tiquete sencillo 500 colones”, “Tiquete
por un día 1000 colones”, etc. Para esto utilice un arreglo
unidimensional.
'''

def control():
    while True:
        respuesta = int(input("\nDigite la opción que desea: \n 1. Volver al menú principal \n 2. Salir \n"))
        if respuesta == 1:
            Menu()
        elif respuesta == 2:
            print("\nGracias por utilizar Radiador Springs S.A.")
            quit()
        else:
            print("\nPor favor digite una opción válida")


def rutas():
    rutas = ["Ruta 1: Coronado - San José","Ruta 2: Guadalupe - San José","Ruta 3: Tibas - San José","Ruta 4: San Pedro - San José","Ruta 5: Santa Marta - San José"]

    
    for ruta in rutas:
        print(ruta)
    ruta_seleccionada = int(input("Seleccione la ruta\n"))

    if 1 <= ruta_seleccionada <= 5:
        return ruta_seleccionada
    print(rutas[ruta_seleccionada - 1])
    #Agregar while y opcion de else


def precios():
    precios = ["Tiquete sencillo: 500 colones", "Tiquete por un día: 1.000 colones", "Tiquete semanal: 6.000 colones", "Tiquete mensual: 20.000 colones"]
    
    
    for precio in precios:
        print(precio)
    Tiquete_seleccionado = int(input("Seleccione el tiquete\n"))

    if 1 <= Tiquete_seleccionado <= 4:
        return Tiquete_seleccionado
    print(precios[Tiquete_seleccionado - 1])
    #Agregar while y opcion de else

def campos(ruta, precio):
    asiento = 1
    matriz = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for x in range(0,5):
        for y in range(0, 2):
            matriz[x][y] = asiento
            asiento += 1
    fila = int(input("Seleccione la fila (1-5): "))
    columna = int(input("Seleccione la columna (1-2): "))
    if 1 <= fila <= 5 and 1 <= columna <= 2:
        print(f"Ha seleccionado el asiento: Fila {fila}, Columna {columna}")
    else:
        print("Selección de asiento no válida.")
    
def espacios():
    print("Espacios disponibles:")
    for fila in campos(0,5):
        for columna in campos(0,2):
            print(f" [{fila + 1}, {columna + 1}]","")
        print()


def Menu():
    rutas1 = ["Ruta 1: Coronado - San José","Ruta 2: Guadalupe - San José","Ruta 3: Tibas - San José","Ruta 4: San Pedro - San José","Ruta 5: Santa Marta - San José"]
    precios1 = ["Tiquete sencillo: 500 colones", "Tiquete por un día: 1.000 colones", "Tiquete semanal: 6.000 colones", "Tiquete mensual: 20.000 colones"]
    while True:
        opcion = int(input("\nDigite la opción que desea: \n 1. Ver Rutas \n 2. Ver Precios \n 3. Adquirir Tiquetes \n 4. Consultar Cantidad de espacios disponibles \n 5. Salir \n "))
        if opcion == 1:
            print(f"\nLas rutas disponibles son:")
            print(rutas1[0])
            print(rutas1[1])
            print(rutas1[2])
            print(rutas1[3])
            print(rutas1[4])
            control()

        elif opcion == 2:
            print(f"\nLos precios disponibles son:")
            print(precios1[0])
            print(precios1[1])
            print(precios1[2])
            print(precios1[3])
            control()

        elif opcion == 3:
            j = 0
            while j < 1:
                respuesta = int(input("Digite la opción que desea: \n 1. Seleccione la ruta \n 2. Volver al menú principal \n 3. Salir \n"))
                if respuesta == 1:
                    ruta_seleccionada = rutas()
                    precio_seleccionado = precios()
                    if ruta_seleccionada and precio_seleccionado:
                        campos(ruta_seleccionada, precio_seleccionado)
                    break
                if respuesta == 2:
                    i = 0
                    j = 1
                elif respuesta == 3:
                    print("Gracias por utilizar Radiador Springs S.A.")
                    i = 1
                    j = 1
                else:
                    print("Por favor digite una opción válida")
                    j = 0

        elif opcion == 4:
            print("Consultar Cantidad de espacios disponibles")
            control()

        elif opcion == 5:
            print("Gracias por utilizar Radiador Springs S.A.")
            False

        else:
            print("\nSeleccione una opción válida")


Menu()
