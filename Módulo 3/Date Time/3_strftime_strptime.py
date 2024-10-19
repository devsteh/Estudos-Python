from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-10-18 20:34"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"
#podemos usar diretivas que retornem informações específicas de data e hora.

#formatação data e hora
print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))


# #conversão de string para datetime de outra forma
# date_string = "28/10/2024 20:34"
# d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
# print(d)