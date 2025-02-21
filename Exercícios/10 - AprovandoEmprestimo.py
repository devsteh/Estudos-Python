renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

limite = renda*0.3

if renda > 2000:
    if parcela <= limite:
        print("Empréstimo aprovado.")
    else:
        print("Empréstimo negado: parcela acima de 30% da renda.")