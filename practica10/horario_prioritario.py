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
    horario = []
    horario.append(materias[0])

    for i in range(1, len(materias)):
        if materias[i]["inicio"] >= horario[-1]["fin"]:
            horario.append(materias[i])
        else:
            if materias[i]["prioridad"] > horario[-1]["prioridad"]:
                horario[-1] = materias[i]                
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

    
ordenar_hora_final(materias) #Funcion para ordenar la lista de materias por orden de prioridad
horario = crear_horario(materias)

for m in horario: #para imprimir el horario
    print("\n")
    print("Materia:", m["nombre"])
    print("Prioridad:", m["prioridad"])
    print("Horario:", m["inicio"], "-", m["fin"])
