import os

rutas1 = ["Ruta 1: Coronado - San José","Ruta 2: Guadalupe - San José","Ruta 3: Tibas - San José","Ruta 4: San Pedro - San José","Ruta 5: Santa Marta - San José"]
precios1 = ["1. Tiquete sencillo: 500 colones", "2. Tiquete por un día: 1.000 colones", "3. Tiquete semanal: 6.000 colones", "4. Tiquete mensual: 20.000 colones"]
matriz1 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz2 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz3 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz4 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
matriz5 = [["1-1", "1-2"], ["2-1", "2-2"], ["3-1", "3-2"], ["4-1", "4-2"], ["5-1", "5-2"]]
    
def control():
    while True:
        respuesta = input("\nDigite la opción que desea: \n 1. Volver al menú principal \n 2. Salir \n")
        if respuesta == "1":
            Menu()
            break
        elif respuesta == "2":
            print("\nGracias por utilizar Radiador Springs S.A.")
            break
        else:
            print("\nPor favor digite una opción válida")


def rutas(rutas1):
    while True:
        try:
            for ruta in rutas1:
                print(ruta)
            ruta_seleccionada = int(input("\nSeleccione la ruta que desea (1-5):\n"))

            if 1 <= ruta_seleccionada <= 5:
                return ruta_seleccionada
            else:
                print("\nPor favor digite una opción válida\n")
        except:
            print("\nPor favor digite una opción válida\n")
        


def precios(precios1):
    while True:
        try:
            for precio in precios1:
                print(precio)
            Tiquete_seleccionado = int(input("\nSeleccione el tipo de tiquete que desea (1-4):\n"))

            if 1 <= Tiquete_seleccionado <= 4:
                return Tiquete_seleccionado
            else:
                print("\nPor favor digite una opción válida\n")
        except:
            print("\nPor favor digite una opción válida\n")


def campos(matriz, precio, ruta_seleccionada):
    while True:
        try:
            cantidad = int(input("\nDigite la cantidad de tiquetes que desea (1-10): \n"))
            if 1 <= cantidad <= 10:
                print("\n")

                for r in range (0,cantidad):
                    while True:
                        try:
                            for x in range (0,5):
                                for y in range (0,2):
                                    print(matriz[x][y],end= " ")
                                print("\n")
                                
                            x = int(input("Seleccione la fila que desea (1-5): \n"))
                            y = int(input("Seleccione la columna que desea (1-2): \n"))
                            if 1 <= x <= 5 and 1 <= y <= 2:
                                x -= 1
                                y -= 1
                                if matriz[x][y] != "O":
                                    matriz[x][y] = "O"
                                    print(f"\nHa seleccionado el asiento: Fila {x + 1}, Columna {y + 1}\n")
                                    break
                                else:
                                    print("\nEl espacio seleccionado ya está ocupado\n")
                            else:
                                print("\nSelección de asiento no válida.\n")
                        except:
                            print("\nSelección de asiento no válida.\n")
                            

                #validación para imprimir el dato correcto en el detalle de la compra
                if precio == 500:
                    tipo = precios1[0]
                elif precio == 1000:
                    tipo = precios1[1]
                elif precio == 6000:
                    tipo = precios1[2]
                elif precio == 20000:
                    tipo = precios1[3]

                #validación para imprimir el dato correcto en el detalle de la compra
                if ruta_seleccionada == 1:
                    ruta = rutas1[0]
                elif ruta_seleccionada == 2:
                    ruta = rutas1[1]
                elif ruta_seleccionada == 3:
                    ruta = rutas1[2]
                elif ruta_seleccionada == 4:
                    ruta = rutas1[3]
                elif ruta_seleccionada == 5:
                    ruta = rutas1[4]
                    
                subtotal = cantidad * precio
                iva = subtotal * 0.13
                total = subtotal + iva

                archivo = open("Factura.txt","w")
                archivo.write("\nDetalle de su compra\n")
                archivo.write(f"Cantidad de tiquetes comprados: {cantidad}\n")
                archivo.write(f"Tipo de tiquetes: {tipo}\n")
                archivo.write(f"{ruta}\n")
                archivo.write(f"Subtotal: {subtotal} colones\n")
                archivo.write(f"IVA: {iva} colones\n")
                archivo.write(f"Total: {total} colones\n")
                archivo.close()

                archivo = open("Control ventas.txt","a")
                archivo.write("\nDetalle de su compra\n")
                archivo.write(f"Cantidad de tiquetes comprados: {cantidad}\n")
                archivo.write(f"Tipo de tiquetes: {tipo}\n")
                archivo.write(f"{ruta}\n")
                archivo.write(f"Subtotal: {subtotal} colones\n")
                archivo.write(f"IVA: {iva} colones\n")
                archivo.write(f"Total: {total} colones\n")
                archivo.close()

                print("Detalle de su compra:")
                print(f"Cantidad de tiquetes comprados: {cantidad}")
                print(f"Tipo de tiquetes: {tipo}")
                print(f"{ruta}")
                print(f"Subtotal: {subtotal}" )
                print(f"IVA: {iva} " )
                print(f"Total: {total}" )

                break
            else:
                print("El máximo de tiquetes que puede comprar es 10")
        except:
            print("\nPor favor digite una opción válida\n")
    
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
        opcion = input("\nDigite la opción que desea: \n 1. Ver Rutas \n 2. Ver Precios \n 3. Adquirir Tiquetes \n 4. Consultar Cantidad de espacios disponibles \n 5. Salir \n ")
        if opcion == "1":
            print(f"\nLas rutas disponibles son:")
            for ruta in rutas1:
                print(ruta)
            control()
            break

        elif opcion == "2":
            print(f"\nLos precios disponibles son:")
            for precio in precios1:
                print(precio)
            control()
            break

        elif opcion == "3":
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
                campos(matriz, precio, ruta_seleccionada)
            control()
            break

        elif opcion == "4":
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
            break

        elif opcion == "5":
            print("Gracias por utilizar Radiador Springs S.A.")
            break

        else:
            print("\nSeleccione una opción válida")


Menu()
