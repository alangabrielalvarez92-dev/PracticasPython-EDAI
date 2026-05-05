matriz_lab = [
    [1,1,0,0,0],
    [1,1,0,1,1],
    [1,'S',0,0,0],
    [1,1,0,1,1],
    [1,1,0,0,'F']
]

def buscar_camino(matriz_lab,fila,columna):
    
    #Casos Base

    if not (0 <= fila <= 4 and 0 <= columna <= 4): #La posición está fuera del laberinto
        return False

    if matriz_lab[fila][columna] == 'F': #Se encontró la salida
        print("Se encontró el final")
        return True
    
    if matriz_lab[fila][columna] == 1 or matriz_lab[fila][columna] == '*': #Si es que ya se visitó
        return False
    
    # Marcar la posición actual como parte del camino
    if matriz_lab[fila][columna] != 'S':
        matriz_lab[fila][columna] = '*'
    
    #Caso recursivo arriba, derecha, abajo, izquierda
    # Arriba
    if buscar_camino(matriz_lab, fila - 1, columna):
        return True
    
    # Derecha
    if buscar_camino(matriz_lab, fila, columna + 1):
        return True

    #Abajo
    if buscar_camino(matriz_lab, fila + 1, columna):
        return True

    #Izquierda
    if buscar_camino(matriz_lab, fila, columna - 1 ):
        return True

    #Si no es ninguna se desmarca el camino
    if matriz_lab[fila][columna] != 'S':
        matriz_lab[fila][columna] = 0
    
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

for fila in matriz_lab:
        print(fila)        