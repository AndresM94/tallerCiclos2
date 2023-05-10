ancho = int(input("Digite el ancho del rombo:\n"))

if ancho % 2 != 0:
    for i in range(1, ancho+1, 2):
        espacios = " " * ((ancho - i) // 2)
        asteriscos = "*" * i
        print(espacios + asteriscos)

    for i in range(ancho-2, 0, -2):
        espacios = " " * ((ancho - i) // 2)
        asteriscos = "*" * i
        print(espacios + asteriscos)
else:
    print("El ancho debe ser un numero impar")