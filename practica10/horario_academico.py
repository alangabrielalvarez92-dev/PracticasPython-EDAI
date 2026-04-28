materias = [] #lista materias que va a guardar cada diccionario que corresponde a cada materia


def ordenar_hora_final(materias): #Ordena de acuerdo a la hora final. Es O(n^2) en el peor caso
    for i in range(1, len(materias)):
        actual = materias[i]
        j = i - 1

        while j >= 0 and materias[j]["fin"] > actual["fin"]:
            materias[j + 1] = materias[j]
            j -= 1

        materias[j + 1] = actual
    
def crear_horario(materias):
    horario = [] #lista para almacenar el horario sin empalmes y respetando el orden de prioridad

    for i in range(len(materias)):
        if materias[i]["prioridad"] == 5:
            materia = materias[i]
            horario.append(materia)
        

    return horario

        

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
    
ordenar_prioridad(materias) #Funcion para ordenar la lista de materias por orden de prioridad

for m in materias: #para imprimir el horario
    print("Materia:", m["nombre"])
    print("Prioridad:", m["prioridad"])
    print("Horario:", m["inicio"], "-", m["fin"])
