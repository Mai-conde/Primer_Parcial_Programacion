from funciones_parcial import *

from Validate_parcial import *

nombres = ["Maite","Diego","Pedro","Lara","Martin","Sofia","Marta","Arturo","Rafael","Kira","Mirta","Beto","Julio","Fabian","Tomas","Maria","Paloma","Malena","Lucas","Mateo","Roman","Daniel","Luna","Paula","Alma","Luz","Paz","Erica","Adrian","Delia"]
generos = ["F","M","M","X","M","F","F","M","X","X","F","M","M","M","X","F","F","F","M","M","X","X","F","F","F","X","X","F","M","F"]
legajos = ["11111", "12111","11211","11121","11112","21111","21211","21121","21112","31111","32111","31211","31121","31112","33111","31311","31131","31113","41111","42111","41211","41121","41112","43111","43211","41311","41131","41113","41132","41321",]
notas = [[6,5,7,4,5],
         [3,5,7,8,6],
         [4,6,8,9,8],
         [6,7,7,7,8],
         [5,6,2,9,6],
         [2,5,9,5,4],
         [4,4,6,7,5],
         [4,9,8,6,2],
         [1,5,8,4,2],
         [2,4,10,8,7],
         [3,7,8,4,9],
         [5,7,9,8,10],
         [5,7,6,7,7],
         [4,6,10,7,5],
         [5,8,9,6,8],
         [5,7,6,6,6],
         [5,7,3,9,9],
         [9,6,5,1,4],
         [4,7,6,9,8],
         [3,5,4,2,8],
         [8,9,6,2,7],
         [5,10,7,8,6],
         [4,1,3,2,5],
         [3,5,8,3,6],
         [7,8,3,9,8],
         [10,4,8,9,7],
         [6,7,5,9,1],
         [5,7,8,4,9],
         [7,4,10,6,1],
         [7,5,7,7,8]]

def menu_de_opciones():

    datos_cargados = False

    promedio_calculado = False
    
    lista_ordenada = False

    while True:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        eleccion = input("\nIngrese un número para realizar una función: \n [1] para ingresar todos los datos\n "
        "[2] para mostrar todos los datos \n "
        "[3] para ver los promedios de los estudiantes \n "
        "[4] para ordenar los promedios de los estudiantes \n "
        "[5] para mostrar la/las materias con mayor promedio general \n" \
        "[6] para buscar y mostrar todos los datos por legajo \n" \
        "[7] para mostrar la cantidad de veces que se repite una nota en una materia determinada  \n " \
        "[8] para salir del programa" \
        "->  ")
        print()
        print("-----------------------------------------------------------------------------------------------------------------------------")

        while validate_number(eleccion) == False:
            print("-----------------------------------------------------------------------------------------------------------------------------")
            eleccion = input("\nError. Ingrese un número valido del 1 al 8: \n [1] para ingresar todos los datos\n "
            "[2] para mostrar todos los datos \n "
            "[3] para ver los promedios de los estudiantes \n "
            "[4] para ordenar los promedios de los estudiantes \n "
            "[5] para mostrar la/las materias con mayor promedio general \n" \
            "[6] para buscar y mostrar todos los datos por legajo \n" \
            "[7] para mostrar la cantidad de veces que se repite una nota en una materia determinada  \n " \
            "[8] para salir del programa" \
            "->   ")
            print()
            print("-----------------------------------------------------------------------------------------------------------------------------")
        
        eleccion = int(eleccion)

        match eleccion:
            case 1: 
                matriz_datos = cargar_datos_estudiantes()
                nombres = matriz_datos[1]
                generos = matriz_datos[2]
                legajos = matriz_datos[3]
                notas = matriz_datos[4]
                datos_cargados = True
                print("\nLOS DATOS SE HAN CARGADO CORRECTAMENTE\n")
            case 2:
                if datos_cargados == True:
                    if lista_ordenada == True:
                        mostrar_todos_los_estudiantes(nombres_originales,generos_originales,legajos_originales,notas_originales)
                    else:
                        mostrar_todos_los_estudiantes(nombres, generos, legajos, notas)
                else:
                    print("Error. No ha cargado los datos")
            case 3:
                if datos_cargados == True:
                    promedios = promedio_notas(notas)
                    print("PROMEDIOS DE CADA ESTUDIANTE\n\n")
                    mostrar_lista(promedios)
                    promedio_calculado = True
                else:
                    print("Error. No ha cargado los datos")
            case 4:
                if datos_cargados == True and promedio_calculado == True:
                    nombres_originales = copiar_lista(nombres)
                    legajos_originales = copiar_lista(legajos)
                    generos_originales = copiar_lista(generos)
                    promedios_originales = copiar_lista(promedios)
                    notas_originales = copiar_matriz(notas)
                    ordenar_lista(promedios,nombres,generos,legajos)
                    lista_ordenada = True
                    print("PROMEDIOS ORDENADOS\n\n")
                    mostrar_datos(nombres,promedios,generos,legajos) 

                else:
                    print("Error. No ha cargado los datos o no se ha calculado el promedio")
            case 5:
                if datos_cargados == True and promedio_calculado == True:
                    promedios_de_materias = promedios_materias(notas)
                    print("PROMEDIO MAYOR ENTRE LAS MATERIAS \n\n")
                    mostrar_materia_mayor_promedio(promedios_de_materias)
                else:
                    print("Error. No ha cargado los datos o no se ha calculado el promedio")
            case 6: 
                if datos_cargados == True and promedio_calculado == True:
                    indice_buscado = buscar_por_legajo(legajos_originales)
                    if indice_buscado != -1:
                        mostrar_datos_segun_legajo_con_notas(indice_buscado,nombres_originales,legajos_originales,generos_originales,notas_originales,promedios_originales)
                else:
                    print("Error. No ha cargado los datos o no se ha calculado el promedio")
            case 7:
                if datos_cargados == True and promedio_calculado == True:
                    numero_de_materia = input("Ingrese el numero de materia en la que desea contar las notas: ")
                    while validate_numero_materia(numero_de_materia) == False:
                        numero_de_materia = input("Ingrese el numero de materia en la que desea contar las notas: ")
                    numero_de_materia = int(numero_de_materia)
                    lista_notas = iteraciones_de_notas(notas,numero_de_materia)
                    print(F"CANTIDAD DE VECES QUE SE REPITE UNA NOTA EN LA MATERIA {numero_de_materia} \n\n")
                    mostrar_lista(lista_notas)
                else:
                    print("Error. No ha cargado los datos o no se ha calculado el promedio")
            case 8:
                break
            case _:
                print("Error, ingrese un numero válido del 1 al 8.")



menu_de_opciones()


