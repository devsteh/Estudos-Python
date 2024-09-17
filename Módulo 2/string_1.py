nome =  "Stephany"

print(nome.upper()) #Todas as letras maiúsculas
print(nome.lower()) #Todas as letras minúsculas
print(nome.title()) #Primeira letra maiúscula

texto = "   Hello World!   "
print(texto)
print(texto.strip()) #Remove espaços do início de do fim 
print(texto.rstrip()) #Remove espaços da direita 
print(texto.lstrip()) #Remove espaços da esquerda

#Centralização com e sem caracteres adicionais e Junções
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))

print(".".join(menu))