matriz_lab = [
    [1,1,0,0,0],
    [1,1,0,1,1],
    [1,'S',0,0,0],
    [1,1,0,1,1],
    [1,1,0,0,'F']
]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

fila = int(input("Ingresa la fila de inicio: "))
columna = int(input("Ingresa la columna de inicio: "))

print("\nMatriz original:")
imprimir_matriz(matriz_lab)

def buscar_camino(matriz_lab, fila, columna):

    if not (0 <= fila <= 4 and 0 <= columna <= 4):
        return False

    if matriz_lab[fila][columna] == 'F':
        print("Se encontró el final")
        return True

    if matriz_lab[fila][columna] == 1 or matriz_lab[fila][columna] == 'X':
        return False

    if matriz_lab[fila][columna] != 'S':
        matriz_lab[fila][columna] = 'X'

    # Arriba
    nueva_fila = fila - 1
    nueva_columna = columna

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 0 or matriz_lab[nueva_fila][nueva_columna] == 'F':
            if buscar_camino(matriz_lab, nueva_fila, nueva_columna):
                matriz_lab[fila][columna] = '*'
                return True

    # Derecha
    nueva_fila = fila
    nueva_columna = columna + 1

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 0 or matriz_lab[nueva_fila][nueva_columna] == 'F':
            if buscar_camino(matriz_lab, nueva_fila, nueva_columna):
                matriz_lab[fila][columna] = '*'
                return True

    # Abajo
    nueva_fila = fila + 1
    nueva_columna = columna

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 0 or matriz_lab[nueva_fila][nueva_columna] == 'F':
            if buscar_camino(matriz_lab, nueva_fila, nueva_columna):
                matriz_lab[fila][columna] = '*'
                return True

    # Izquierda
    nueva_fila = fila
    nueva_columna = columna - 1

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 0 or matriz_lab[nueva_fila][nueva_columna] == 'F':
            if buscar_camino(matriz_lab, nueva_fila, nueva_columna):
                matriz_lab[fila][columna] = '*'
                return True

    return False


if buscar_camino(matriz_lab, fila, columna):
    print("\nSí hay camino")
else:
    print("\nNo hay camino")

print("\nMatriz final:")
imprimir_matriz(matriz_lab)
            