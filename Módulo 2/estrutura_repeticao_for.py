#EXEMPLO FOR
# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")
        
# print()

#EXEMPLO FOR ELSE
#texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:   
    print()
    print("Executou no fim do laço")
    
#EXEMPLO USANDO A FUNÇÃO BUILT-IN RANGE COM FOR
for numero in range(0, 51, 5):
    print (numero, end="")