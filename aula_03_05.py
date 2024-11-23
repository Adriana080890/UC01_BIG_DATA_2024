# Programa de 
idade = int(input('Informe a idade:'))
peso = float(input('Informe o seu peso (kg):'))
sono = int(input('O quanto você dormiu nas últimas 24horas?:'))
if (idade >= 16) and (idade <= 69):
    if ( peso > 50) and ( sono > 6):
        Print ( 'Doador aprovado')
else:
    Print ( 'Doador reprovado') 
  