materias = [] #lista materias que va a guardar cada diccionario que corresponde a cada materia

def ordenar_prioridad(materias):
    for i in range(1, len(materias)):
        actual = materias[i]
        j = i - 1

        while j >= 0 and materias[j]["prioridad"] < actual["prioridad"]:
            materias[j + 1] = materias[j]
            j -= 1

        materias[j + 1] = actual
    


print("----Horario Académico----")

#Ciclo para almacenar los datos 
for i in range(1,6): #Se van a almacenar 5 materias 
    #Entrada de datos
    print("Ingresa la materia ", i)
    nombre = input("Nombre: ")
    prioridad = int(input("Prioridad: "))
    inicio = int(input("Hora inicio: "))
    fin = int(input("Hora fin: "))

    materia = { #Diccionario materia
        "nombre": nombre,
        "prioridad": prioridad,
        "inicio": inicio,
        "fin": fin
    }

    materias.append(materia) #cada diccionario se va a almacenar en la lista materias
    
ordenar_prioridad(materias)

for m in materias:
    print("Materia:", m["nombre"])
    print("Prioridad:", m["prioridad"])
    print("Horario:", m["inicio"], "-", m["fin"])
