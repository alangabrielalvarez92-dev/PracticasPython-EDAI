def suma(a, b):
    return a + b


suma_lambda = lambda a, b: a + b


while True:
    print("\n--- MENÚ ---")
    print("1. Usar función normal")
    print("2. Usar función lambda")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = int(input("Ingresa un número: "))
        b = int(input("Ingresa otro número: "))
        print("Resultado con función def:", suma(a, b))

    elif opcion == "2":
        a = int(input("Ingresa un número: "))
        b = int(input("Ingresa otro número: "))
        print("Resultado con función lambda:", suma_lambda(a, b))

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")