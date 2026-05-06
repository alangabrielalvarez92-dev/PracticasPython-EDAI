matriz_lab = [
    [1,1,0,0,0],
    [1,1,0,1,1],
    [1,'S',0,0,0],
    [1,1,0,1,1],
    [1,1,0,0,'F']
]

def imprimir_matriz(matriz):
    print()
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()
    print("-" * 15)

def buscar_camino(matriz_lab, fila, columna):
    # Caso base: fuera de la matriz
    if fila < 0 or fila >= 5 or columna < 0 or columna >= 5:
        return False

    # Caso base: pared o visitado
    if matriz_lab[fila][columna] == 1 or matriz_lab[fila][columna] == '*':
        return False

    # Caso base: salida
    if matriz_lab[fila][columna] == 'F':
        print("Se encontró la salida")
        return True

    # Marcar la posición actual
    if matriz_lab[fila][columna] != 'S':
        matriz_lab[fila][columna] = '*'
        print(f"Marcando posición ({fila}, {columna})")
        imprimir_matriz(matriz_lab)

    # Probar arriba
    if buscar_camino(matriz_lab, fila - 1, columna):
        return True

    # Probar abajo
    if buscar_camino(matriz_lab, fila + 1, columna):
        return True

    # Probar izquierda
    if buscar_camino(matriz_lab, fila, columna - 1):
        return True

    # Probar derecha
    if buscar_camino(matriz_lab, fila, columna + 1):
        return True

    # Si ningún camino funcionó, desmarcar
    if matriz_lab[fila][columna] != 'S':
        matriz_lab[fila][columna] = 0
        print(f"Retrocediendo desde ({fila}, {columna})")
        imprimir_matriz(matriz_lab)

    return False

while True:
    fila = int(input("Ingresa la fila de inicio: "))
    columna = int(input("Ingresa la columna de inicio: "))

    if 0 <= fila <= 4 and 0 <= columna <= 4:
        break
    else:
        print("Ingresa solo datos dentro de los valores del 0 al 4")

if buscar_camino(matriz_lab, fila, columna):
    print("Se encontró la salida")
else:
    print("No se encontró salida")