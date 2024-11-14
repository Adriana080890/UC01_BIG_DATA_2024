# Idade a partir do ano de nascimento
import datetime # Importa a biblioteca datetime
data_atual = datetime.date.today() # Armazena a data completa
nasc = int(input('Digite o ano que você nasceu:'))
ano_atual = data_atual.year # armazena a varuavek do ano atual. 
print(ano_atual)
idade = ano_atual - nasc
print(f' A Sua idade é {idade}anos')