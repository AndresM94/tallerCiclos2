digito1 = int(input("Digite el primer digito 1:\n"))
digito2 = int(input("Digite el primer digito 2:\n"))

if digito1 < digito2:
    cont2 = digito1
    while cont2 <= digito2:
        cont = 1
        divisores = 0
        while cont <= cont2:
            if cont2 % cont == 0:
                divisores += 1
            cont += 1
        if divisores <= 2:
            print(cont2, end=" ")
        cont2 += 1
else:
    cont2 = digito2
    while cont2 <= digito1:
        cont = 1
        divisores = 0
        while cont <= cont2:
            if cont2 % cont == 0:
                divisores += 1
            cont += 1
        if divisores <= 2:
            print(cont2, end=" ")
        cont2 += 1