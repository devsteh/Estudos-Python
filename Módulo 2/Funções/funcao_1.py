def exibir_mensagem():
    print("Hello World!")
    
def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")
    
def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
    
exibir_mensagem()
exibir_mensagem2(nome="Ste")
exibir_mensagem3() #se não for apontado algum valor, retornará o que foi atribuido na função
exibir_mensagem3(nome="Stephany") #Caso contrário, será retornado o valor passado na chamada da funçào