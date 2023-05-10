candidato1 = 0
candidato2 = 0
candidato3 = 0
votoEnBlanco = 0
votoNulo = 0
cantidadDeVotos = 0
ganador = ""
votosGanador = 0
while True:
    eleccion = int(input("""Elige el candidato por el que votas:
    1. Candidato 1
    2. Candidato 2
    3. Candidato 3
    4. Voto en blanco\n"""))

    if eleccion == 1:
        candidato1 += 1
    elif eleccion == 2:
        candidato2 += 1
    elif eleccion == 3:
        candidato3 += 1
    elif eleccion == 4:
        votoEnBlanco += 1
    else:
        votoNulo += 1
    cantidadDeVotos += 1
    opcion = input("Deseas volver a votar (s/n):\n").lower()
    if opcion == "n":
        break

if candidato1 > votosGanador:
    ganador = "Candidato 1"
    votosGanador = candidato1
elif candidato2 > votosGanador:
    ganador = "Candidato 2"
    votosGanador = candidato2
elif candidato3 > votosGanador:
    ganador = "Candidato 3"
    votosGanador = candidato3
elif votoEnBlanco > votosGanador:
    ganador = "Voto en blanco"
    votosGanador = votoEnBlanco

porcentaje = (votosGanador / cantidadDeVotos) * 100

if votosGanador > 0:
    print("----- Resultados De La Votacion -----")
    print(f"""Los votos quedaron asi:
    Candidato 1: {candidato1}
    Candidato 2: {candidato2}
    Candidato 3: {candidato3}
    Voto en blanco: {votoEnBlanco}
    Voto nulo: {votoNulo}
    Votos totales: {cantidadDeVotos}""")
    print(f"Y el ganador es {ganador} con {votosGanador} votos, con un porcentaje de {porcentaje:.2f}% de {cantidadDeVotos} total de votos")
else:
    print("Nadie a ganado")
