peso = float(input("Digite seu peso: "))
altura =  float(input("Digite sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"Você está abaixo do peso. IMC: {imc}")
elif imc <= 18.5 or imc < 25:
    print(f"Você está com o peso normal. IMC: {imc}")
elif imc >= 25:
    print(f"Você está acima do peso. IMC: {imc}")