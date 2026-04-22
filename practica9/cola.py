cola = []

while True:
    print("\n--- MENÚ ---")
    print("1. Encolar")
    print("2. Desencolar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Ingresa 5 números:")
        for i in range(1, 5):
            n = int(input("Ingresa el número : "))
            cola.append(n)

    elif opcion == "2":
        elemento = cola.pop(0)
        print("Elemento eliminado:", elemento)
        print("Cola final:", cola)

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")
