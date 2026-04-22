while True:
    print("\n--- MENÚ ---")
    print("1. Contar del 1 al 5")
    print("2. Mostrar números pares hasta un número")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Contando del 1 al 5:")
        for i in range(1, 6):
            print(i)

    elif opcion == "2":
        n = int(input("Ingresa un número: "))
        print("Números pares:")
        i = 0
        while i <= n:   
            print(i)
            i += 2

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")