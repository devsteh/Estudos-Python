nome = "Stephany"
idade = 24
profissao = "Programadora"
linguagem = "Python"

#Exemplo old style (%) não é comumente utilizado
# %s = string
# %d = valores inteiros
# %f = valores de ponto flutuante

print ("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou estudando %s." %(nome, idade, profissao, linguagem))

#Exemplo format
print ("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou estudando {3}." .format(nome, idade, profissao, linguagem))
print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou estudando {}." .format(nome, idade, profissao, linguagem))

##Ambos acima podem causar bagunça ao acabar trocando a ordem das variáveis de forma acidental

#Exemplo f strings
print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou estudando {linguagem}.")

#Formatação strings com f strings
PI = 3.14159

print(f"O valor de PI é: {PI:.2f}")
print(f"O valor de PI é: {PI:10.2f}")

