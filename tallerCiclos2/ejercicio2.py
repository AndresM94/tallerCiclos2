tieneCuenta = False
cantidad = 0
errores = []
correctos = []

while True:
    opcion = int(input("""Que deseas hacer:
    1. Depositar
    2. Retirar
    3. Abrir Cuenta
    4. Cerrar Cuenta\n"""))

    if opcion == 1:
        if tieneCuenta:
            cantidadDepositar = float(input("¿Cuanto deseas depositar?\n"))
            cantidad += cantidadDepositar
            print("Depositado de manera correcta")
            correctos.append("Depositado de manera correcta")
        else:
            print("No se puede depositar por que no tienes cuenta")
            errores.append("No se puede depositar por que no tienes cuenta")
    elif opcion == 2:
        if tieneCuenta:
            cantidadRetirar = float(input("¿Cuanto deseas retirar?\n"))
            if cantidadRetirar <= cantidad:
                cantidad -= cantidadRetirar
                print(f"Retiraste con exito ${cantidadRetirar}")
                correctos.append(f"Retiraste con exito ${cantidadRetirar}")
            else:
                print("No se puede retirar por que el monto a retirar es mayor al saldo de la cuenta")
                errores.append("No se puede retirar por que el monto a retirar es mayor al saldo de la cuenta")
        else:
            print("No se puede retirar por que no tienes cuenta")
            errores.append("No se puede retirar por que no tienes cuenta")
    elif opcion == 3:
        if tieneCuenta:
            print("No puedes crear una cuenta por que ya la tienes creada")
            errores.append("No puedes crear una cuenta por que ya la tienes creada")
        else:
            tieneCuenta = True
            print("Cuenta creada de manera exitosa")
            correctos.append("Cuenta creada de manera exitosa")
    elif opcion == 4:
        if tieneCuenta:
            if cantidad > 0:
                print(f"No se puede cerrar cuenta por que tiene ${cantidad} de dinero en la cuenta")
                errores.append(f"No se puede cerrar cuenta por que tiene ${cantidad} de dinero en la cuenta")
            else:
                tieneCuenta = False
                print("Cuenta cerrada de manera exitosa")
                correctos.append("Cuenta cerrada de manera exitosa")
        else:
            print("No se puede cerrar una cuenta que no ha sido creada")
            errores.append("No se puede cerrar una cuenta que no ha sido creada")
    continua = input("Deseas continuar: (y/n)\n").lower()
    if continua == "n":
        print("Adios")
        break
if len(correctos) > 0:
    for correcto in correctos:
        print(correcto)

if len(errores) > 0:
    for error in errores:
        print(error)

if tieneCuenta:
    print(f"Tu saldo es ${cantidad}")
else:
    print("No tienes cuenta abierta por lo tal no tienes saldo")
