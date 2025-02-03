nome = input("Digite seu nome: ")
idade = input ("Infome sua idade:")

print (nome, idade)
print (nome, idade, end="...\n")
print (nome, idade, sep="#", end="...\n")
print (nome, idade, sep="#")
print (f"Bem vindo, {nome}! Sua idade é {idade} anos!")