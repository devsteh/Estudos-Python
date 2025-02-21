distancia = int(input("Digite a distância percorrida (em KM): "))

if distancia <= 100:
    print(f"O valor do pedágio é de R$10,00. Distância percorrida: {distancia} KM")
elif distancia <= 200:
    print(f"O valor do pedágio é de R$20,00. Distância percorrida: {distancia} KM")
elif distancia > 200:
    print(f"O valor do pedágio é de R$30,00. Distância percorrida: {distancia} KM")

