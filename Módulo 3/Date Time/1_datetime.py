from datetime import date, datetime, time
#Forma mais prática da importação da funções

data = (date(2024, 10, 5))
print(data)
print(date.today()) #Data atual

data_hora = datetime (2024, 10, 10, 11, 40, 00) 
#Não passando o parâmetro de hora, virá zerado no print
print(data_hora)
print(datetime.today())

#Retorna hora, passando parâmetros
hora = time (11, 40, 0)
print(hora)