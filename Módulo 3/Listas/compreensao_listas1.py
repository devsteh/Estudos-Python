numeros = [1, 30, 21, 2, 9, 65,34]

pares1 = []

for numero in numeros:
    if numero %2 == 0:
        pares1.append(numero)

print(pares1)

#Compreension list
numeros = [1, 30, 21, 2, 9, 65,34]
pares = [numero for numero in numeros if numero %2 == 0]

print(pares)