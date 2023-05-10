filas = int(input("Digite el numero de filas:\n"))

for i in range(filas):
    print("*"*(i+1))

for i in range(filas-1, 0, -1):
    print("*"*(i))