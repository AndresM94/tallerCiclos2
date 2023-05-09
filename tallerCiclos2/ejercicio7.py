filas = int(input("Digite el numero de filas:\n"))

for i in range(filas):
    print("*"*(i+1),"     ", "*"*(filas-i),"*"*(filas-i),"     ", "*"*(i+1))