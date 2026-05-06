def fib(num):
    f1 = 0
    f2 = 1
    for i in range(1, num-1):
        f1,f2=f2,f1+f2 #asignación paralela
    return f2

print(fib(5))