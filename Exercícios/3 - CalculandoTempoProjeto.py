A = int(input("Informe os dias para a atividade A: "))
B = int(input("Informe os dias para a atividade B: "))
C = int(input("Informe os dias para a atividade C: "))

tempo =  A + B + C

if  A <= -0:
    print("Os dias de atividades não podem ser negativos.")
elif B <= -0:
    print("Os dias de atividades não podem ser negativos.")
elif C <= -0:
    print("Os dias de atividades não podem ser negativos.")
elif tempo:
    print(f"O tempo total do projeto é de {tempo} horas")