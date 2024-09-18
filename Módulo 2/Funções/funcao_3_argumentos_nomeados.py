def salvar_carro(marca, modelo, ano, placa):
    #salvando carro...
    print(f"Veículo cadastrado com sucesso! \n Dados: {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Chevrolet", "Prisma", 2012, "ABC-1234")
salvar_carro(marca="Chevrolet", modelo="Prisma", ano=2012, placa="ABC-1234")
salvar_carro(**{"marca": "Chevrolet", "modelo": "Prisma", "ano": 2012, "placa": "ABC-1234"})