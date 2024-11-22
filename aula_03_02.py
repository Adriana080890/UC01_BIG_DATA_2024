# Programa média com desvio 
nome = (input('Informe o seu nome:'))
n1 = float(input(' Informe sua nota:'))
n2 = float(input(' Informe sua nota:'))
media = (n1 + n2) / 2
if media > 70:
    print(f'SR.(a){nome}, ua média foi {media}, portanto você está aprovado (a), parabéns!')
elif media >=30:
    print(f'SR.(a){nome}, sua média foi {media}, portanto você está em recuperação')
else:
    print(f'SR.(a){nome}, ua média foi {media}, portantovocê está reprovado(a), estude mais!')