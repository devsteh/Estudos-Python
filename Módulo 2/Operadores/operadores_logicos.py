# AND = para ser TRUE, tudo precisa ser TRUE
# OR = para ser TRUE, apenas um prescisa ser TRUE
print (True and True)
print (True and False)
print (True or True)
print (True or False)
print (False or False)
print (False and False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print (exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp2)
