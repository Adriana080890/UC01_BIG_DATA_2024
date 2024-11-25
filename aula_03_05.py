# Programa de 
from cgi import print_arguments


idade = int(input('Informe a idade:'))
peso = float(input('Informe o seu peso (kg):'))
sono = int(input('O quanto você dormiu nas últimas 24horas?:'))
if (idade >= 16) and (idade <= 69) and ( peso >= 50) and ( sono >= 6):
        print('Doador Aprovado')
else:
    print('Doador reprovado, não atende as exigencias mínimas') 
  