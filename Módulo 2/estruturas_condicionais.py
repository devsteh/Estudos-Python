MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

# EXEMPLO IF
# if idade >= 18:
#     print ("Você pode tirar sua CNH.")

# if idade < MAIOR_IDADE:
#     print("Ainda não pode tirar sua CNH.")
    
    
# EXEMPLO IF ELSE    
# if idade >= MAIOR_IDADE:
#     print ("Você pode tirar sua CNH.")

# else:
#     print("Ainda não pode tirar sua CNH.")
  
  
# EXEMPLO IF ELIF ELSE  
if idade >= MAIOR_IDADE:
     print ("Você pode tirar sua CNH.")
elif idade == IDADE_ESPECIAL:
     print ("Você pode fazer suas aulas teóricas, mas não pode fazer aulas práticas.")
else:
     print("Ainda não pode tirar sua CNH.")
     
