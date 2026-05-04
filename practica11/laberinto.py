matriz_lab = [
    ['S',0,1,0,0],
    [1,0,0,1,0],
    [0,1,0,0,'F']
]

fila = int(input("Ingresa la fila de inicio: "))
columna = int(input("Ingresa la columna de inicio: "))

def buscar_camino(matriz_lab,fila,columna):
    
    # Arriba
    nueva_fila = fila - 1
    nueva_columna = columna

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4: #Se verifica que no se salga de la matriz
        if matriz_lab[nueva_fila][nueva_columna] == 'F':
            print("Se encontró el final")
            return
        
        elif matriz_lab[nueva_fila][nueva_columna] == 0: #Se revisa si hay camino arriba
            return buscar_camino(matriz_lab, nueva_fila, nueva_columna) #Si hay camino se vuelve a llamar a la función



    # Derecha
    nueva_fila = fila
    nueva_columna = columna + 1

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 'F':
            print("Se encontró el final")
            return
        elif matriz_lab[nueva_fila][nueva_columna] == 0:
            return buscar_camino(matriz_lab, nueva_fila, nueva_columna)

    # Abajo
    nueva_fila = fila + 1
    nueva_columna = columna

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 'F':
            print("Se encontró el final")
            return
        elif matriz_lab[nueva_fila][nueva_columna] == 0:
            return buscar_camino(matriz_lab, nueva_fila, nueva_columna)

    # Izquierda
    nueva_fila = fila
    nueva_columna = columna - 1

    if 0 <= nueva_fila <= 4 and 0 <= nueva_columna <= 4:
        if matriz_lab[nueva_fila][nueva_columna] == 'F':
            print("Se encontró el final")
            return
        elif matriz_lab[nueva_fila][nueva_columna] == 0:
            return buscar_camino(matriz_lab, nueva_fila, nueva_columna)
        
    return buscar_camino(matriz_lab, nueva_fila, nueva_columna)         

            