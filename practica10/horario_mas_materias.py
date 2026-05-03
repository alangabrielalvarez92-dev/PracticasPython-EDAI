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

    for materia in materias:
        if not horario:
            horario.append(materia)
        else:
            ultima = horario[-1] #se guarda en una variable temporal la última materia que se registró en la lista horario

            if materia["inicio"] >= ultima["fin"]: #Se verifica si no hay enpalme 
                horario.append(materia) #si no hay se agrega
            else: #si hay enpalme se le indica al usuario que desea agregar al horario

                print("\nError: Se empalman las siguientes materias...")
                print(f"1. {ultima['nombre']} Prioridad: {ultima['prioridad']}")
                print(f"2. {materia['nombre']} Prioridad: {materia['prioridad']}")

                opcion = input("¿Qué materia quieres inscribir? (1 o 2): ")

                if opcion == "2":
                    horario[-1] = materia 

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
    print("\n")

    materia = { #Diccionario materia
        "nombre": nombre,
        "prioridad": prioridad,
        "inicio": inicio,
        "fin": fin
    }

    materias.append(materia) #cada diccionario se va a almacenar en la lista materias
  
ordenar_hora_final(materias) 
horario = crear_horario(materias)

for i in range(0,len(horario)): #para imprimir el horario
    print("\n")
    print("Materia:", horario[i]["nombre"])
    print("Prioridad:", horario[i]["prioridad"])
    print("Horario:", horario[i]["inicio"], "-", horario[i]["fin"])

