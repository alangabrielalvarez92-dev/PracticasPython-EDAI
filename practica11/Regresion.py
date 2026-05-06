def cuenta_regresiva(n):
    if n == 0:
        print("Fin")
        return
    print("Entrando con:", n)
    cuenta_regresiva(n-1)
    print("Saliendo con:", n)

cuenta_regresiva(5)