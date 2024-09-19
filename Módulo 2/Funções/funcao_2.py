def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

def frase():
    print ("Praticando chamada de funções com Python")

print(calcular_total([10,20,34]))
print(retorna_antecessor_sucessor(10)) #Retornará em tupla, pois é uma estrutura imutável
print(frase()) #Retorno none quando não há retorno em função



