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

for Hospital in Hospitales:
    Hospitales[Hospital] = merge_sort(Hospitales[Hospital])

for alumno in alumnos:
    alumnos[alumno] = merge_sort(alumnos[alumno])



#print(Hospitales["Hospital B"][1][1])
#print(len(Hospitales))
#print(merge_sort(str))