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



def validate_numero_materia(numero_materia):
    flag = True
    if validate_number(numero_materia) == False:
        flag = False
    else:
        numero_materia = int(numero_materia)
        if numero_materia > 5 or numero_materia < 1:
            flag = False
    return flag