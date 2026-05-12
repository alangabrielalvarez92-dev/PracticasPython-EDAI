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


def gale_shapley(Hospitales,alumnos):
    hospitales_libres = list(Hospitales.keys()) #se guardan las claves
    siguiente_propuesta = {hospital: 0 for hospital in Hospitales}



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

siguiente_propuesta = {hospital: 0 for hospital in Hospitales}
print(siguiente_propuesta.items())