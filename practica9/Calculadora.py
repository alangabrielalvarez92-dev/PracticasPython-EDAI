print("=== Calculadora Básica ===")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("\nSelecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. División entera")

opcion = input("Opción: ")

if opcion == "1":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

elif opcion == "2":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")

elif opcion == "3":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")

elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Error: No se puede dividir entre cero")

elif opcion == "5":
    resultado = num1 ** num2
    print(f"Resultado: {resultado}")

elif opcion == "6":
    if num2 != 0:
        resultado = num1 // num2
        print(f"Resultado: {resultado}")
    else:
        print("Error: No se puede dividir entre cero")

else:
    print("Opción no válida")
