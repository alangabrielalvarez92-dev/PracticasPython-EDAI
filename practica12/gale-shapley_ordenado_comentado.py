# Define una funcion llamada merge_sort que recibe una lista llamada st.
def merge_sort(st):
    # Si la lista tiene 0 o 1 elementos, ya esta ordenada.
    if len(st) <= 1:
        # Regresa la misma lista sin hacer cambios.
        return st

    # Calcula la mitad de la lista para dividirla en dos partes.
    mid = len(st) // 2

    # Ordena recursivamente la mitad izquierda de la lista.
    izquierda = merge_sort(st[:mid])
    # Ordena recursivamente la mitad derecha de la lista.
    derecha = merge_sort(st[mid:])

    # Une las dos mitades ya ordenadas en una sola lista ordenada.
    return merge(izquierda, derecha)


# Define una funcion llamada merge que mezcla dos listas ya ordenadas.
def merge(izq, der):
    # Crea una lista vacia donde se guardara el resultado ordenado.
    resultado = []
    # i recorrera la lista izquierda y j recorrera la lista derecha.
    i = j = 0

    # Mientras todavia haya elementos en ambas listas, se comparan entre si.
    while i < len(izq) and j < len(der):
        # Compara el puntaje de cada tupla; el indice 1 es el puntaje.
        if izq[i][1] > der[j][1]:
            # Si el puntaje de la izquierda es mayor, agrega ese elemento primero.
            resultado.append(izq[i])
            # Avanza al siguiente elemento de la lista izquierda.
            i += 1
        else:
            # Si el puntaje de la derecha es mayor o igual, agrega ese elemento primero.
            resultado.append(der[j])
            # Avanza al siguiente elemento de la lista derecha.
            j += 1

    # Agrega los elementos restantes de la lista izquierda, si quedaron algunos.
    resultado.extend(izq[i:])
    # Agrega los elementos restantes de la lista derecha, si quedaron algunos.
    resultado.extend(der[j:])

    # Regresa la lista completa ordenada de mayor a menor puntaje.
    return resultado


# Define una funcion que transforma preferencias con puntajes en preferencias solo con nombres.
def obtener_nombres(preferencias):
    # Crea un diccionario vacio para guardar las preferencias ordenadas.
    preferencias_ordenadas = {}

    # Recorre cada persona o entidad y su lista de preferencias.
    for persona, lista in preferencias.items():
        # Ordena la lista de preferencias usando merge_sort.
        lista_ordenada = merge_sort(lista)
        # Guarda solo los nombres, quitando los puntajes de las tuplas.
        preferencias_ordenadas[persona] = [opcion[0] for opcion in lista_ordenada]

    # Regresa el diccionario con listas ordenadas solo por nombres.
    return preferencias_ordenadas


# Define la funcion principal del algoritmo Gale-Shapley.
def gale_shapley(hospitales, alumnos):
    # Crea una lista con todos los hospitales que aun no tienen alumno asignado.
    hospitales_libres = list(hospitales.keys())
    # Crea un diccionario donde se guardara el emparejamiento alumno -> hospital.
    emparejamiento = {}
    # Guarda en que posicion de su lista va cada hospital para saber a quien proponer despues.
    siguiente_propuesta = {hospital: 0 for hospital in hospitales}

    # Crea un diccionario para saber rapidamente que hospital prefiere cada alumno.
    ranking = {}
    # Recorre cada alumno y su lista de hospitales preferidos.
    for alumno, lista in alumnos.items():
        # Convierte la lista de preferencias en un ranking numerico.
        ranking[alumno] = {
            # La posicion mas baja significa mayor preferencia.
            hospital: posicion for posicion, hospital in enumerate(lista)
        }

    # El algoritmo continua mientras existan hospitales libres.
    while hospitales_libres:
        # Toma el primer hospital libre de la lista.
        hospital = hospitales_libres.pop(0)

        # Busca el siguiente alumno al que este hospital todavia no le ha propuesto.
        alumno = hospitales[hospital][siguiente_propuesta[hospital]]
        # Avanza el contador para que la proxima vez proponga al siguiente alumno.
        siguiente_propuesta[hospital] += 1

        # Si el alumno no tiene hospital asignado, acepta la propuesta.
        if alumno not in emparejamiento:
            # Guarda que este alumno queda emparejado con este hospital.
            emparejamiento[alumno] = hospital
        else:
            # Si el alumno ya tenia hospital, se obtiene el hospital actual.
            hospital_actual = emparejamiento[alumno]

            # Compara si el alumno prefiere el nuevo hospital sobre el hospital actual.
            if ranking[alumno][hospital] < ranking[alumno][hospital_actual]:
                # Si prefiere el nuevo hospital, cambia su emparejamiento.
                emparejamiento[alumno] = hospital
                # El hospital anterior queda libre y vuelve a la lista.
                hospitales_libres.append(hospital_actual)
            else:
                # Si el alumno prefiere su hospital actual, rechaza al nuevo hospital.
                hospitales_libres.append(hospital)

    # Crea un nuevo diccionario para mostrar el resultado como hospital -> alumno.
    resultado = {}
    # Recorre el emparejamiento que estaba guardado como alumno -> hospital.
    for alumno, hospital in emparejamiento.items():
        # Invierte el orden para guardar hospital -> alumno.
        resultado[hospital] = alumno

    # Regresa el emparejamiento final.
    return resultado


# Diccionario de hospitales; cada hospital tiene alumnos con puntajes.
Hospitales = {
    # El Hospital A prefiere a Ana con 90, Sofia con 85 y Luis con 70.
    "Hospital A": [("Ana", 90), ("Luis", 70), ("Sofia", 85)],
    # El Hospital B prefiere a Luis con 95, Ana con 80 y Sofia con 60.
    "Hospital B": [("Ana", 80), ("Luis", 95), ("Sofia", 60)],
    # El Hospital C prefiere a Sofia con 100, Ana con 75 y Luis con 65.
    "Hospital C": [("Ana", 75), ("Luis", 65), ("Sofia", 100)]
}

# Diccionario de alumnos; cada alumno tiene hospitales con puntajes.
alumnos = {
    # Ana prefiere Hospital A con 95, Hospital B con 80 y Hospital C con 70.
    "Ana": [("Hospital A", 95), ("Hospital B", 80), ("Hospital C", 70)],
    # Luis prefiere Hospital B con 100, Hospital C con 75 y Hospital A con 60.
    "Luis": [("Hospital A", 60), ("Hospital B", 100), ("Hospital C", 75)],
    # Sofia prefiere Hospital C con 90, Hospital A con 85 y Hospital B con 65.
    "Sofia": [("Hospital A", 85), ("Hospital B", 65), ("Hospital C", 90)],
}

# Ordena las preferencias de hospitales y deja solo los nombres de los alumnos.
Hospitales = obtener_nombres(Hospitales)
# Ordena las preferencias de alumnos y deja solo los nombres de los hospitales.
alumnos = obtener_nombres(alumnos)

# Ejecuta Gale-Shapley con las preferencias ya ordenadas.
resultado = gale_shapley(Hospitales, alumnos)

# Imprime un titulo para las preferencias de hospitales.
print("Preferencias de hospitales ordenadas:")
# Recorre cada hospital y su lista de preferencias ya ordenada.
for hospital, preferencias in Hospitales.items():
    # Muestra el hospital y sus alumnos preferidos en orden.
    print(hospital, "->", preferencias)

# Imprime un titulo para las preferencias de alumnos.
print("\nPreferencias de alumnos ordenadas:")
# Recorre cada alumno y su lista de preferencias ya ordenada.
for alumno, preferencias in alumnos.items():
    # Muestra el alumno y sus hospitales preferidos en orden.
    print(alumno, "->", preferencias)

# Imprime un titulo para el resultado final.
print("\nEmparejamiento final:")
# Recorre cada hospital y el alumno que le fue asignado.
for hospital, alumno in resultado.items():
    # Muestra la pareja final hospital - alumno.
    print(hospital, "-", alumno)

# Ejemplo de consulta: mostraria el puntaje del segundo alumno del Hospital B en la version original.
# print(Hospitales["Hospital B"][1][1])
# Ejemplo de consulta: mostraria cuantos hospitales hay.
# print(len(Hospitales))
# Ejemplo de prueba: ordenaria una lista llamada str si existiera.
# print(merge_sort(str))
