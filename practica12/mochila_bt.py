objetos = [
    ("Laptop", 3, 90),
    ("Libro", 1, 30),
    ("Ropa", 2, 50),
    ("Camara", 2, 70),
    ("Audifonos", 1, 40)
]

capacidad = 5

mejor_valor = 0
mejor_combinacion = []


def mochila_backtracking(i, peso_actual, valor_actual, elegidos):
    global mejor_valor, mejor_combinacion

    if i == len(objetos):
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_combinacion = elegidos.copy()
        return

    nombre, peso, valor = objetos[i]

    # Opcion 1: meter el objeto
    if peso_actual + peso <= capacidad:
        elegidos.append(nombre)

        mochila_backtracking(
            i + 1,
            peso_actual + peso,
            valor_actual + valor,
            elegidos
        )

        elegidos.pop()

    # Opcion 2: no meter el objeto
    mochila_backtracking(i + 1, peso_actual, valor_actual, elegidos)


mochila_backtracking(0, 0, 0, [])

print("---- Mochila Backtracking ----")
print("Mejor valor:", mejor_valor)
print("Objetos elegidos:", mejor_combinacion)