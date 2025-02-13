limite = 3000.00
despesas = float(input("Digite o total das suas despesas este mês: "))

if despesas < limite or despesas == limite:
    print(f"Parabéns, você não ultrapassou o limite de orçamento. Valor gasto: {despesas}")
elif despesas > limite:
    print(f"Atenção! Você ultrapassou o limite de orçamento. Valor gasto: {despesas}")