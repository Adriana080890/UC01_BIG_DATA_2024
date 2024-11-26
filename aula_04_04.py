# 
soma = 0
media = 0
num_maior = 0
nome_maior = 10
for i in range (3):
    nome = (input("Informe seu nome: "))
    idade = int(input("Informe sua idade:"))
    if idade > num_maior:
       num_maior = idade 
       nome_maior = nome
    soma = soma + idade # Acumulador
media = soma / (i + 1)  # i começa com Zero e por isso soma 1
print(f" O resultado da soma das idades é {soma} e a média das idades é {media:.2f} anos")
print(f' A pessoa mais velha é {nome_maior}')