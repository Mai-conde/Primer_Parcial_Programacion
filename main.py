from paquete_ejemplo.funciones import *


bienvenida = input("Ingrese 'OK' para elegir una operacion aritmetica: ")
continuar = "Desea continuar realizando otra operacion aritmetica (si/no)?: "

while True:
    if bienvenida == "OK":
        seleccion = input("Sleccione la operación a realizar (suma/resta/producto/cociente): ")
        a = int(input("Ingrese el primer número entero: "))
        b = int(input("Ingrese el segundo número entero: "))
    
        match seleccion:
            case "suma":
                print(suma(a,b))
            case "resta":
                print(resta(a,b))
            case "producto":
                print(producto(a,b))
            case "cociente":
                print(cociente(a,b))
            case _:
                seleccion = input("Ingrese una operacion válida (suma/resta/producto/cociente): ")

        input(continuar)

        if continuar == "si":
            continue
        else:
            break
    else:
        input("Error, ingrese 'ok' si desea realizar una operación aritmetica")
