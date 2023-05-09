n = int(input("Digite un numero cualquiera:\n"))
a, b = 0, 1
cont = 0
while cont < n:
    print(a, end=" ")
    a, b = b, a+b
    cont += 1
