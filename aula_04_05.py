#
for i in range (3):
    nome = (input("Informe seu nome:"))
    n1 = float(input("Informe primeira nota:"))
    n2 = float(input("Informe segunda nota:"))
    média = (n1 + n2) / 2
    if média >= 70:
        print(f'{nome}sua média é {média}, você está Aprovado.')
    elif média >= 30:
        print(f'{nome}sua média é {média}, você está RECUPERAÇÃO.')  
    else:
        print(f'{nome}sua média é {média}, você está Reprovado.')