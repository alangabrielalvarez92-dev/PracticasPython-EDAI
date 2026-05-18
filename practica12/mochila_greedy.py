objetos = [
    ("Laptop", 3, 90),
    ("Libro", 1, 30),
    ("Ropa", 2, 50),
    ("Camara", 2, 70),
    ("Audifonos", 1, 40)
]

capacidad = 5


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2

    izquierda = merge_sort(lista[:mid])
    derecha = merge_sort(lista[mid:])

    return merge(izquierda, derecha)


def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        razon_izq = izq[i][2] / izq[i][1]
        razon_der = der[j][2] / der[j][1]

        if razon_izq > razon_der:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado


def mochila_voraz(objetos, capacidad):
    objetos_ordenados = merge_sort(objetos)

    peso_total = 0
    valor_total = 0
    elegidos = []

    for objeto in objetos_ordenados:
        nombre, peso, valor = objeto

        if peso_total + peso <= capacidad:
            elegidos.append(nombre)
            peso_total += peso
            valor_total += valor

    return elegidos, peso_total, valor_total


elegidos, peso_total, valor_total = mochila_voraz(objetos, capacidad)

print("---- Mochila Voraz ----")
print("Valor total:", valor_total)
print("Peso total:", peso_total)
print("Objetos elegidos:", elegidos)