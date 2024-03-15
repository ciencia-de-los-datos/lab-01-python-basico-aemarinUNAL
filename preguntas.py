"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import fileinput
filename = 'data.csv'
lines = []
with fileinput.input(files=filename, encoding='utf-8') as f:
    for line in f:
        lines.append(line.split())


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    suma = 0
    for l in lines:
        suma += int(l[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    letter_count = {}
    for line in lines:
        letter = line[0]
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return sorted(letter_count.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    suma_letra = {}
    for line in lines:
        letra = line[0]
        num = int(line[1])
        if letra in suma_letra:
            suma_letra[letra] += num
        else:
            suma_letra[letra] = num
    return sorted(suma_letra.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    month_count = {}
    for l in lines:
        month = l[2].split('-')[1]
        if month in month_count:
            month_count[month] += 1
        else:
            month_count[month] = 1
    return sorted(month_count.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    letter_values = {}
    
    for l in lines:
        letter = l[0]
        num = int(l[1])
        
        if letter in letter_values:
            letter_values[letter] = (max(letter_values[letter][0], num), min(letter_values[letter][0], num))
        else:
            letter_values[letter] = (num, num)
    return sorted([(keys, values[0], values[1]) for keys, values in letter_values.items()])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    values_letter = {}
    for l in lines:
        for k_v in l[4].split(','):
            key, value = k_v.split(':')
            value = int(value) 

            if key not in values_letter:
                values_letter[key] = {'min': value, 'max': value}
            else:
                values_letter[key]['min'] = min(values_letter[key]['min'], value)
                values_letter[key]['max'] = max(values_letter[key]['max'], value)
    return sorted([(key, values['min'], values['max']) for key, values in values_letter.items()])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    values_letters = {}
    for l in lines:
        value = int(l[1])
        letter = l[0]
        if value not in values_letters:
            values_letters[value] = [letter]
        else:
            values_letters[value].append(letter)
    list_value_key = [(k, v) for k, v in values_letters.items()]
    return sorted(list_value_key)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    values_letters = {}
    for l in lines:
        num = int(l[1]) 
        letter = l[0] 
        if num not in values_letters:
            values_letters[num] = {letter}
        else:
            values_letters[num].add(letter)
    return sorted([(num, sorted(list(letter))) for num, letter in values_letters.items()], key=lambda x: x[0])


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    key_count = {}
    for l in lines:
        element = l[4].split(',')
        for e in element:
            k, _ = e.split(':')
            if k in key_count:
                key_count[k] += 1
            else:
                key_count[k] = 1
    return key_count


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    listado = []
    for l in lines:
        letter = l[0]
        elements_col4 = len(l[3].split(','))
        elements_col5 = len(l[4].split(','))
        listado.append((letter, elements_col4, elements_col5))
    return listado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    suma_por_letra = {}
    for l in lines:
        v = int(l[1])
        letters = l[3].split(',')
        for letter in letters:
            if letter not in suma_por_letra:
                suma_por_letra[letter] = v
            else:
                suma_por_letra[letter] += v
    return {letter: suma for letter, suma in sorted(suma_por_letra.items())}


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_letra = {}
    for l in lines:
        letra = l[0] 
        elements = l[4].split(',')
        suma_valores = sum(int(e.split(':')[1]) for e in elements)
        if letra in suma_por_letra:
            suma_por_letra[letra] += suma_valores
        else:
            suma_por_letra[letra] = suma_valores
    return {letter: suma for letter, suma in sorted(suma_por_letra.items())}