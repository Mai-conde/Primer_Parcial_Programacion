def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial=0) -> list:
    '''  Documentación:
    Objetivo: Inicializar una matriz de n filas por m columnas.

    Parámetros:
        cant_filas (int): Cantidad de filas de la nueva matriz
        cant_columnas (int): Cantidad de columnas de la nueva matriz
    Retorno:
        list: retorna la matriz inicializada'''
    
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz

def inicializar_lista(cant_elementos:int,valor_inicial = 0) -> list:
    '''  Documentación:
    Objetivo: Inicializar una lista de n elementos.

    Parámetros:
        cant_elementos (int): Cantidad de elementos de la nueva lista
    Retorno:
        list: retorna la lista inicializada'''
    
    lista = [valor_inicial] * cant_elementos
    for i in range(cant_elementos):
        lista[i] = i
    
    return lista

def mostrar_matriz(matriz:list) -> None:
    '''  Documentación:
    Objetivo: mostrar una matriz

    Parámetros:
        matriz (list): Matriz que quiere mostrarse'''
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

def mostrar_lista(lista:list) -> None:
    '''  Documentación:
    Objetivo: mostrar una lista

    Parámetros:
        lista (list): lista que quiere mostrarse'''
    
    for i in range(len(lista)):
        print(lista[i], end=" ")

def validate_number(cadena) -> bool:
    '''  Documentación:
    Objetivo: validar un numero

    Parámetros:
        cadena (Any): cadena a validar
    Retorno:
        bool: retorna True si es un numero, y False si no lo es'''
    
    flag = True
    for elemento in cadena:
        if ord(elemento) < 48 or ord(elemento) > 57:
            flag = False
            break

    return flag

def validate_str(cadena) -> bool:
    '''Documentación:
    Objetivo: validar una cadena

    Parámetros:
        cadena (str): cadena a validar
    Retorno:
        bool: retorna True si es una cadena, y False si no lo es'''
    
    flag = True
    for i in cadena:
        if ord(i) >= 48 and ord(i) <= 57: 
            flag = False
    return flag

def validate_genero(genero:str) -> bool:
    '''Documentación:
    Objetivo: validar un genero

    Parámetros:
        genero (str): genero a validar
    Retorno:
        bool: retorna True si es un genero, y False si no lo es'''
    
    flag = True
    if genero != "F" and genero != "M" and genero != "X":
        flag = False
    return flag

def validate_legajo(legajo:str) -> bool:
    '''Documentación:
    Objetivo: validar un legajo

    Parámetros:
        legajo (str): legajo a validar
    Retorno:
        bool: retorna True si es un legajo, y False si no lo es'''
    
    flag = True
    if validate_number(legajo) == False:
        flag = False
    else:
        legajo = int(legajo)
        if legajo > 99999 or legajo < 9999:
            flag = False
    return flag

def validate_nota(nota) -> bool:
    '''Documentación:
    Objetivo: validar una nota

    Parámetros:
        nota (Any): nota a validar
    Retorno:
        bool: retorna True si es una nota, y False si no lo es'''
    flag = True
    if nota > 10 or nota < 1:
        flag = False
    return flag

def cargar_datos_estudiantes(cantidad_estudiantes=30) -> list:
    '''Documentación:
    Objetivo: cargar los datos de todos los estudiantes

    Parámetros:
        cantidad_estudiantes: cantidad de estudiantes a cargar
    retorna:
        matriz (list): Matriz completa con todos los datos
        nombres (list): Lista de todos los nombres cargados
        generos (list): Lista de todos los generos cargados
        legajos (list): Lista de todos los legajos cargados
        notas (list): Lista de todas las notas cargados
        '''
    matriz = inicializar_matriz(cantidad_estudiantes, 8) 
    nombres = inicializar_lista(cantidad_estudiantes)
    generos = inicializar_lista(cantidad_estudiantes)
    legajos = inicializar_lista(cantidad_estudiantes)
    notas = inicializar_matriz(cantidad_estudiantes, 5)

    for i in range(cantidad_estudiantes):
        print(f"--- Ingresando datos del estudiante {i+1} ---")
        j = 0

        nombre = input("Ingrese el nombre: ")
        while validate_str(nombre) == False:
            nombre = input("Error, nombre inválido. Ingrese un nombre válido: ")
        matriz[i][j] = nombre
        nombres[i] = nombre
        j += 1

        genero = input("Ingrese el género (F, M, X): ")
        while validate_genero(genero) == False:
            genero = input("Error, género inválido. Ingrese un género válido (F, M, X): ")
        matriz[i][j] = genero
        generos[i] = genero
        j += 1

        legajo = input("Ingrese el legajo: ")
        while validate_legajo(legajo) == False:
            legajo = input("Error, legajo inválido. Asegúrese de ingresar un número de 5 cifras: ")
        matriz[i][j] = legajo
        legajos[i] = legajo
        j += 1

        for k in range(5):
            nota = int(input(f"Ingrese la nota {k+1}: "))
            while validate_nota(nota) == False:
                nota = int(input(f"Error, nota inválida. Ingrese la nota {k+1} nuevamente (entre el 1 y el 10): "))
            matriz[i][j] = nota
            notas[i][k] = nota
            j += 1

    print("Ha finalizado la carga de datos")

    return matriz, nombres, generos, legajos, notas

def mostrar_un_estudiante(nombres:list, generos:list, legajos:list, notas:list, numero_estudiante:int) -> None:
    '''Documentación:
    Objetivo: mostrar los datos de un estudiante en particular

    Parámetros:
        nombres (list): lista de nombres 
        generos (list): lista de generos 
        legajos (list): lista de legajos 
        notas (list): matriz de notas 
        numero estudiante (int): numero del estudiante a mostrar
        '''
    
    print(f"{nombres[numero_estudiante]}\t  {generos[numero_estudiante]}\t  {legajos[numero_estudiante]} \t" , end="")
    for nota in notas[numero_estudiante]:
        print(nota, end=" ")
    print()

def mostrar_todos_los_estudiantes(nombres:list, generos:list, legajos:list, notas:list) -> None:
    '''Documentación:
    Objetivo: mostrar los datos de todos los estudiantes

    Parámetros:
        nombres (list): lista de nombres 
        generos (list): lista de generos 
        legajos (list): lista de legajos 
        notas (list): matriz de notas 
        '''
    for i in range(len(notas)):
        mostrar_un_estudiante(nombres,generos,legajos,notas,i)
        print()

def promedio_notas(matriz:list) -> list:
    '''Documentación:
    Objetivo: calcular el promedio de las notas de cada estudiante

    Parámetros:
        matriz (list): matriz de notas
    retorna:
        promedios (list): Lista de todos los promedios 
        '''
    promedios = inicializar_lista(len(matriz))
    for i in range(len(matriz)):
        suma = 0
        for nota in matriz[i]:
            suma += nota
        promedio = suma / len(matriz[i])
        promedios[i] = promedio
    return promedios

def ordenar_asc(promedio:list, nombre:list, genero:list, legajo:list) -> None:
    '''Documentación:
    Objetivo: ordenar los datos de todos los estudiantes de manera ascendente

    Parámetros:
        promedio (list): lista de los promedios
        nombre (list): lista de los nombres
        genero (list): lista de los generos
        legajo (list): lista de los promedios
        '''
    for i in range(0, len(promedio)-1, 1):
        for j in range(i + 1, len(promedio), 1):
            if promedio[i] > promedio[j]:
                promedio_auxiliar = promedio[i]
                promedio[i] = promedio[j]
                promedio[j] = promedio_auxiliar

                nombre_auxiliar = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = nombre_auxiliar

                genero_auxiliar = genero[i]
                genero[i] = genero[j]
                genero[j] = genero_auxiliar

                legajo_auxiliar = legajo[i]
                legajo[i] = legajo[j]
                legajo[j] = legajo_auxiliar

def ordenar_desc(promedio:list, nombre:list, genero:list, legajo:list) -> None:
    '''Documentación:
    Objetivo: ordenar los datos de todos los estudiantes de manera descendente

    Parámetros:
        promedio (list): lista de los promedios
        nombre (list): lista de los nombres
        genero (list): lista de los generos
        legajo (list): lista de los promedios
        '''
    for i in range(0, len(promedio)-1, 1):
        for j in range(i + 1, len(promedio), 1):
            if promedio[i] < promedio[j]:
                promedio_auxiliar = promedio[i]
                promedio[i] = promedio[j]
                promedio[j] = promedio_auxiliar

                nombre_auxiliar = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = nombre_auxiliar

                genero_auxiliar = genero[i]
                genero[i] = genero[j]
                genero[j] = genero_auxiliar

                legajo_auxiliar = legajo[i]
                legajo[i] = legajo[j]
                legajo[j] = legajo_auxiliar

def mostrar_datos(nombres:list, promedios:list, generos:list, legajos:list) -> None:
    '''Documentación:
    Objetivo: mostrar los datos de todos los estudiantes 

    Parámetros:
        nombres (list): lista de los nombres
        promedios (list): lista de los promedios
        generos (list): lista de los generos
        legajos (list): lista de los promedios
        '''
    for i in range(len(promedios)):
        if len(nombres[i]) < 8:
            print(f"{nombres[i]}\t\t{promedios[i]}\t{generos[i]}\t{legajos[i]}")
        else:
            print(f"{nombres[i]}\t{promedios[i]}\t{generos[i]}\t{legajos[i]}")

def validate_criterio(criterio:str) -> bool:
    '''  Documentación:
    Objetivo: validar un criterio

    Parámetros:
        criterio (Any): criterio a validar
    Retorno:
        bool: retorna True si es un criterio válido, y False si no lo es'''
    
    flag = True
    if criterio != "desc" and criterio != "DESC" and criterio != "ASC" and criterio != "asc":
        flag = False
    return flag

def ordenar_lista(promedio:list, nombre:list, genero:list, legajo:list, criterio = "DESC") -> None:
    '''Documentación:
    Objetivo: ordenar los datos de todos los estudiantes 

    Parámetros:
        promedio (list): lista de los promedios
        nombre (list): lista de los nombres
        genero (list): lista de los generos
        legajo (list): lista de los promedios
        criterio (str): criterio de ordenamiento (ascendente o descendente)
        '''
    if validate_criterio(criterio) == False:
        print("Error, el criterio no es válido")
    else:
        if criterio == "DESC" or criterio == "desc":
            ordenar_desc(promedio,nombre,genero,legajo)
        else:
            ordenar_asc(promedio,nombre,genero,legajo)

def promedios_materias(notas:list) -> list:
    '''Documentación:
    Objetivo: calcular el promedio de las notas por materia

    Parámetros:
        notas (list): matriz de notas
    retorna:
        promedios (list): Lista de todos los promedios 
        '''
    
    promedios = inicializar_lista(len(notas[0]))
    for j in range(len(notas[0])):
        suma = 0
        for i in range(len(notas)):
            suma += notas[i][j]
        promedio = suma / len(notas)
        promedios[j] = promedio
    return promedios

def indice_mayor_promedio_por_materia(promedios:list) -> list:
    '''Documentación:
    Objetivo: hallar el o los indices que corresponden a las materias con mayor promedio

    Parámetros:
        promedios (list): lista de promedios de materias
    retorna:
        posiciones (list): Lista que contiene a los indices que correspondan a la materia con mayor promedio
        '''
    maximo = promedios[0]
    for i in range(len(promedios)):
        if promedios[i] > maximo:
            maximo = promedios[i]
    posiciones = [-1]*len(promedios)
    contador = 0
    for i in range(len(promedios)):
        if promedios[i] == maximo:
            posiciones[contador] = i
            contador += 1
    return posiciones

def lista_mayor_promedio(promedios:list):
    '''Documentación:
    Objetivo: crear una nueva lista que solo guarde los indices correspondientes a las materias con mayor promedio

    Parámetros:
        promedios (list): lista de promedios de materias
    retorna:
        posiciones (list): Lista que contiene solo a los indices que correspondan a la materia con mayor promedio
        '''
    posiciones = indice_mayor_promedio_por_materia(promedios)
    contador = 0
    for dato in posiciones:
        if dato > -1:
            contador += 1
    lista_max_promedio = [-1]*contador
    
    j = 0
    for i in range(len(posiciones)):
        if posiciones[i] > -1:
            lista_max_promedio[j] = posiciones[i]
            j += 1
    return lista_max_promedio

def mostrar_materia_mayor_promedio(promedios:list) -> None:
    '''Documentación:
    Objetivo: mostrar las materias con mayor promedio (y el promedio)

    Parámetros:
        promedios (list): lista de promedios de materias
        '''
    lista_max_promedio = lista_mayor_promedio(promedios)
    materias = [0]*len(lista_max_promedio)
    for i in range(len(lista_max_promedio)):
        indice = lista_max_promedio[i]
        materias[i] = f"materia {indice + 1}"
        print(f"la {materias[i]} tiene mayor promedio con {promedios[indice]}")

def buscar_por_legajo(legajos:list) -> int:
    '''Documentación:
    Objetivo: buscar un legajo solicitado

    Parámetros:
        legajos (list): lista de promedios de materias
    retorna:
        indice_estudiante (int): indice del legajo encontrado
        indice_estudiante (bool): False si no se encuentra el legajo'''

    indice_estudiante = -1
    legajo_a_buscar = input("Ingrese el legajo que desea buscar: ")
    while validate_legajo(legajo_a_buscar) == -1:
        legajo_a_buscar = input("Error. Ingrese un número de legajo válido a buscar: ")
    
    for i in range(len(legajos)):
        if legajos[i] == legajo_a_buscar:
            indice_estudiante = i
            break
    if legajos[i] != legajo_a_buscar:
        print("no encontrado")
    
    return indice_estudiante

def mostrar_datos_segun_legajo_con_notas(indice:int, nombres:list, legajos:list, generos:list, notas:list, promedios:list) -> None:
    '''Documentación:
    Objetivo: mostrar los datos del estudiantes segun el legajo buscado

    Parámetros:
        indice (int): indice correspondiente al legajo buscado
        nombres (list): lista de los nombres
        legajos (list): lista de los promedios
        generos (list): lista de los generos
        notas (list): matriz de notas
        promedios (list): lista de promedios
        '''   
    
    print(f"{nombres[indice]}\t {generos[indice]}\t {legajos[indice]}\t    {promedios[indice]}\t" , end="\t")
    for nota in notas[indice]:
        print(nota, end=" ")
    print() 
    
def mostrar_datos_segun_legajo(indice:int, nombres:list, legajos:list, generos:list, promedios:list):
    '''Documentación:
    Objetivo: mostrar los datos del estudiantes segun el legajo buscado

    Parámetros:
        indice (int): indice correspondiente al legajo buscado
        nombres (list): lista de los nombres
        legajos (list): lista de los promedios
        generos (list): lista de los generos
        promedios (list): lista de promedios
        '''   
    print(f"{nombres[indice]}\t {generos[indice]}\t {legajos[indice]}\t    {promedios[indice]}\t" , end="\t")
    
