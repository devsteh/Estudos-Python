princesas = {
    "aurora@outlook.com": {"nome": "Aurora", "apelido": "Bela Adormecida", "telefone": "1253-8762"},
    "bela@gmail.com": {"nome": "Bela", "apelido": "Bela da Fera", "telefone": "9175-3743"},
    "valente@yahoo.com": {"nome": "Merida", "apelido": "Valente", "telefone": "7753-1725"},
    "cinderela@gmail.com": {"nome": "Cinderela", "apelido": "Cinderela", "telefone": "3012-7212"},
}

#Passa linha a linha retornando apenas as chaves com o primeiro valor da string
for chave in princesas:
    print(chave, princesas[chave])
    
print("=" * 100)

for chave, valor in princesas.items():
    print(chave, valor)