# Bibliotecas
import random
import matplotlib.pyplot as plt

times = 0


def merge_sort(st):
    if len(st) <= 1:
        return st

    mid = len(st) // 2

    izquierda = merge_sort(st[:mid])
    derecha = merge_sort(st[mid:])

    return merge(izquierda, derecha)


def merge(izq, der):
    global times

    resultado = []

    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        times = times + 1

        if izq[i][1] > der[j][1]:
            resultado.append(izq[i])
            i = i + 1
        else:
            resultado.append(der[j])
            j = j + 1

    while i < len(izq):
        resultado.append(izq[i])
        i = i + 1

    while j < len(der):
        resultado.append(der[j])
        j = j + 1

    return resultado


def obtener_nombres(preferencias):
    preferencias_ordenadas = {}

    for persona in preferencias:
        lista = preferencias[persona]

        lista_ordenada = merge_sort(lista)

        nueva_lista = []

        for opcion in lista_ordenada:
            nombre = opcion[0]
            nueva_lista.append(nombre)

        preferencias_ordenadas[persona] = nueva_lista

    return preferencias_ordenadas


def gale_shapley(hospitales, alumnos):
    global times

    hospitales_libres = list(hospitales.keys())

    emparejamiento = {}

    siguiente_propuesta = {}

    for hospital in hospitales:
        siguiente_propuesta[hospital] = 0

    nivel_preferencias = {}

    for alumno in alumnos:
        lista = alumnos[alumno]

        nivel_preferencias[alumno] = {}

        posicion = 0

        for hospital in lista:
            nivel_preferencias[alumno][hospital] = posicion
            posicion = posicion + 1

    while len(hospitales_libres) > 0:
        hospital = hospitales_libres.pop(0)

        posicion_alumno = siguiente_propuesta[hospital]
        alumno = hospitales[hospital][posicion_alumno]

        siguiente_propuesta[hospital] = siguiente_propuesta[hospital] + 1

        # Se cuenta una propuesta
        times = times + 1

        if alumno not in emparejamiento:
            emparejamiento[alumno] = hospital
        else:
            hospital_actual = emparejamiento[alumno]

            posicion_nuevo = nivel_preferencias[alumno][hospital]
            posicion_actual = nivel_preferencias[alumno][hospital_actual]

            # Se cuenta una comparación de preferencias
            times = times + 1

            if posicion_nuevo < posicion_actual:
                emparejamiento[alumno] = hospital
                hospitales_libres.append(hospital_actual)
            else:
                hospitales_libres.append(hospital)

    resultado = {}

    for alumno in emparejamiento:
        hospital = emparejamiento[alumno]
        resultado[hospital] = alumno

    return resultado

def generar_datos(n):
    hospitales = {}
    alumnos = {}

    nombres_hospitales = []
    nombres_alumnos = []

    for i in range(n):
        nombres_hospitales.append("Hospital " + str(i + 1))
        nombres_alumnos.append("Alumno " + str(i + 1))

    for hospital in nombres_hospitales:
        lista = []

        for alumno in nombres_alumnos:
            puntaje = random.randint(1, 100)
            lista.append((alumno, puntaje))

        hospitales[hospital] = lista

    for alumno in nombres_alumnos:
        lista = []

        for hospital in nombres_hospitales:
            puntaje = random.randint(1, 100)
            lista.append((hospital, puntaje))

        alumnos[alumno] = lista

    return hospitales, alumnos

TAM = 101

eje_x = list(range(1, TAM, 1))
eje_y = []

for num in eje_x:
    hospitales, alumnos = generar_datos(num)

    times = 0

    hospitales = obtener_nombres(hospitales)
    alumnos = obtener_nombres(alumnos)

    resultado = gale_shapley(hospitales, alumnos)

    eje_y.append(times)


fig, ax = plt.subplots(facecolor='w', edgecolor='k')

ax.plot(eje_x, eje_y, marker='o', color="b", linestyle='None')

ax.set_xlabel('Número de hospitales y alumnos')
ax.set_ylabel('Operaciones')
ax.grid(True)
ax.legend(["Gale-Shapley con Merge Sort"])

plt.title('Complejidad del programa Gale-Shapley')
plt.show()