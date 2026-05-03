import time
import random
import matplotlib.pyplot as plt

def generar_materias(n):
    materias = []

    for i in range(n):
        inicio = random.randint(7, 20)
        duracion = random.randint(1, 4)
        fin = inicio + duracion

        materia = {
            "nombre": f"Materia {i + 1}",
            "prioridad": random.randint(1, 5),
            "inicio": inicio,
            "fin": fin
        }

        materias.append(materia)

    return materias


def ordenar_hora_final(materias):
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
            if materia["inicio"] >= horario[-1]["fin"]:
                horario.append(materia)

    return horario


tamanos = [10, 50, 100, 200, 500, 1000]
tiempos = []

for n in tamanos:
    materias = generar_materias(n)

    inicio = time.time()

    ordenar_hora_final(materias)
    horario = crear_horario(materias)

    fin = time.time()

    tiempos.append(fin - inicio)


plt.plot(tamanos, tiempos, marker="o")
plt.xlabel("Cantidad de materias ingresadas")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Tiempo de ejecución en función de los datos ingresados")
plt.grid(True)
plt.show()