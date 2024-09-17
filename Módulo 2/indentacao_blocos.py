def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado com sucesso!")
        print("Retire as cédulas na boca do caixa.")
        
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    
sacar(1000)        