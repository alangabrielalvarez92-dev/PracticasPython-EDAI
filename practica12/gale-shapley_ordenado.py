def merge_sort(st):
    if len(st) <= 1:
        return st
    
    mid = len(st) // 2

    izquierda = merge_sort(st[:mid])
    derecha = merge_sort(st[mid:])

    return merge(izquierda, derecha)

def merge(izq,der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i][1] > der[j][1]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
            
    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado

def obtener_nombres(preferencias):
    preferencias_ordenadas = {}

    for persona, lista in preferencias.items():
        lista_ordenada = merge_sort(lista)
        preferencias_ordenadas[persona] = [opcion[0] for opcion in lista_ordenada]

    return preferencias_ordenadas

def gale_shapley(hospitales, alumnos):
    hospitales_libres = list(hospitales.keys())
    emparejamiento = {}  # alumno -> hospital
    siguiente_propuesta = {hospital: 0 for hospital in hospitales}

    ranking = {}
    for alumno, lista in alumnos.items():
        ranking[alumno] = {
            hospital: posicion for posicion, hospital in enumerate(lista)
        }

    while hospitales_libres:
        hospital = hospitales_libres.pop(0)

        alumno = hospitales[hospital][siguiente_propuesta[hospital]]
        siguiente_propuesta[hospital] += 1

        if alumno not in emparejamiento:
            emparejamiento[alumno] = hospital
        else:
            hospital_actual = emparejamiento[alumno]

            if ranking[alumno][hospital] < ranking[alumno][hospital_actual]:
                emparejamiento[alumno] = hospital
                hospitales_libres.append(hospital_actual)
            else:
                hospitales_libres.append(hospital)

    resultado = {}
    for alumno, hospital in emparejamiento.items():
        resultado[hospital] = alumno

    return resultado

Hospitales = { 
    "Hospital A": [("Ana", 90), ("Luis", 70), ("Sofia", 85)],
    "Hospital B": [("Ana", 80), ("Luis", 95), ("Sofia", 60)],
    "Hospital C": [("Ana", 75), ("Luis", 65), ("Sofia", 100)]
}

alumnos = {
    "Ana": [("Hospital A", 95), ("Hospital B", 80), ("Hospital C", 70)],
    "Luis": [("Hospital A", 60), ("Hospital B", 100), ("Hospital C", 75)],
    "Sofia": [("Hospital A", 85), ("Hospital B", 65), ("Hospital C", 90)],
}

Hospitales = obtener_nombres(Hospitales)
alumnos = obtener_nombres(alumnos)

resultado = gale_shapley(Hospitales, alumnos)

print("Preferencias de hospitales ordenadas:")
for hospital, preferencias in Hospitales.items():
    print(hospital, "->", preferencias)

print("\nPreferencias de alumnos ordenadas:")
for alumno, preferencias in alumnos.items():
    print(alumno, "->", preferencias)

print("\nEmparejamiento final:")
for hospital, alumno in resultado.items():
    print(hospital, "-", alumno)

