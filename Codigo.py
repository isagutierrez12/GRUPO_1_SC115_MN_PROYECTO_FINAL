import os

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

rutas1 = ["Ruta 1: Coronado - San José","Ruta 2: Guadalupe - San José","Ruta 3: Tibas - San José","Ruta 4: San Pedro - San José","Ruta 5: Santa Marta - San José"]
precios1 = ["Tiquete sencillo: 500 colones", "Tiquete por un día: 1.000 colones", "Tiquete semanal: 6.000 colones", "Tiquete mensual: 20.000 colones"]
matriz1 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz2 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz3 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz4 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz5 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
    
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


def rutas(rutas1): 
    for ruta in rutas1:
        print(ruta)
    ruta_seleccionada = int(input("Seleccione la ruta\n"))

    if 1 <= ruta_seleccionada <= 5:
        return ruta_seleccionada
    print(rutas[ruta_seleccionada - 1])
    #Agregar while y opcion de else


def precios(precios1):
    for precio in precios1:
        print(precio)
    Tiquete_seleccionado = int(input("Seleccione el tiquete\n"))

    if 1 <= Tiquete_seleccionado <= 4:
        return Tiquete_seleccionado
    print(precios[Tiquete_seleccionado - 1])
    #Agregar while y opcion de else

def campos(matriz, precio):
    while True:
        cantidad = int(input("Digite la cantidad de tiquetes que desea: "))

        if cantidad <= 10:
            for r in range (cantidad):
            
                for x in range (0,5):
                    for y in range (0,2):
                        print(matriz[x][y],end= " ")
                    print("\n")
                

                x = int(input("Seleccione la fila (1-5): "))
                y = int(input("Seleccione la columna (1-2): "))
                if 1 <= x <= 5 and 1 <= y <= 2:
                    x -= 1
                    y -= 1
                    if matriz[x][y] != "O":
                        matriz[x][y] = "O"
                        print(f"Ha seleccionado el asiento: Fila {x + 1}, Columna {y + 1}")
                    else:
                        print("El espacio seleccionado ya está ocupado")
                else:
                    print("Selección de asiento no válida.")

            subtotal = cantidad * precio
            iva = subtotal * 0.13
            total = subtotal + iva

            archivo = open("Factura.txt","w")
            archivo.write("\nEl detalle de su compra\n")
            archivo.write(f"Cantidad de tiquetes comprados: {cantidad}\n")
            archivo.write(f"Tipo de tiquetes: {precio} colones\n")
            archivo.write(f"Subtotal: {subtotal} colones\n")
            archivo.write(f"iva: {iva} colones\n")
            archivo.write(f"Total: {total} colones\n")
            archivo.close()

            archivo = open("Control ventas.txt","a")
            archivo.write("\nEl detalle de su compra\n")
            archivo.write(f"Cantidad de tiquetes comprados: {cantidad}\n")
            archivo.write(f"Tipo de tiquetes: {precio} colones\n")
            archivo.write(f"Subtotal: {subtotal} colones\n")
            archivo.write(f"iva: {iva} colones\n")
            archivo.write(f"Total: {total} colones\n")
            archivo.close()

            print(f"subtotal: {subtotal}" )
            print(f"iva: {iva} " )
            print(f"total: {total}" )

            break
        else:
            print("El máximo de tiquetes que puede comprar es 10")
    
def espacios(matriz):
    disponibles = 0
    for x in range (0,5):
        for y in range (0,2):
            print(matriz[x][y],end= " ")
        print("\n")
    for x in range (0,5):
        for y in range (0,2):
            if matriz[x][y] != "O":
                disponibles += 1
    print(f"Espacios disponibles: {disponibles}")


def Menu():
    while True:
        opcion = int(input("\nDigite la opción que desea: \n 1. Ver Rutas \n 2. Ver Precios \n 3. Adquirir Tiquetes \n 4. Consultar Cantidad de espacios disponibles \n 5. Salir \n "))
        if opcion == 1:
            print(f"\nLas rutas disponibles son:")
            for ruta in rutas1:
                print(ruta)
            control()

        elif opcion == 2:
            print(f"\nLos precios disponibles son:")
            for precio in precios1:
                print(precio)
            control()

        elif opcion == 3:
            ruta_seleccionada = rutas(rutas1)
            if  ruta_seleccionada == 1:
                matriz = matriz1
            elif ruta_seleccionada == 2:
                matriz = matriz2
            elif ruta_seleccionada == 3:
                matriz = matriz3
            elif ruta_seleccionada == 4:
                matriz = matriz4
            elif ruta_seleccionada == 5:
                matriz = matriz5

            precio_seleccionado = precios(precios1)
            if  precio_seleccionado == 1:
                precio = 500
            elif precio_seleccionado == 2:
                precio = 1000
            elif precio_seleccionado == 3:
                precio = 6000
            elif precio_seleccionado == 4:
                precio = 20000

            if ruta_seleccionada and precio_seleccionado:
                campos(matriz, precio)
            control()

        elif opcion == 4:
            ruta_seleccionada = rutas(rutas1)
            if  ruta_seleccionada == 1:
                matriz = matriz1
            elif ruta_seleccionada == 2:
                matriz = matriz2
            elif ruta_seleccionada == 3:
                matriz = matriz3
            elif ruta_seleccionada == 4:
                matriz = matriz4
            elif ruta_seleccionada == 5:
                matriz = matriz5
            if ruta_seleccionada:
                espacios(matriz)
            control()

        elif opcion == 5:
            print("Gracias por utilizar Radiador Springs S.A.")
            break

        else:
            print("\nSeleccione una opción válida")


Menu()
