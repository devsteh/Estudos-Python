carros = ["gol", "celta", "palio"]

for indice ,carro in enumerate(carros): 
    # quando o enumerate é usado, são apontados 2 parâmetros. 1 será o contador 
    # do índice e o outro será o objeto da lista, no caso índice e carro.
    print (f"{indice}: {carro}")