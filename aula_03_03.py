# Informar nome, sexo e idade (Exemplo de conectivo)
nome = (input('Informe seu nome:'))
sexo = (input('Informe seu sexo (M ou F):'))
idade = int(input('Informe a idade:'))
if (idade >= 18) and (sexo == "M" or sexo == 'm'):
    Certificado = int(input(' Informe o certificado de reservista:'))
elif idade >= 18:
     print('Você é maior de idade')
else:
    print('Você é menor de idade')