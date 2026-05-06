def busqueda(lista, objetivo, inicio, fin):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    elif objetivo < lista[medio]:
        return busqueda(lista, objetivo, inicio, medio-1)
    else:
        return busqueda(lista, objetivo, medio+1, fin)
    
datos = [1,3,4,5,7,9]
print(busqueda(datos, 7, 0, len(datos)-1))