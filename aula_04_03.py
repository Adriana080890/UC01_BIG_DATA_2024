# Programa que realiza a soma dentro 5 números inteiros r fornrcr o maior valor 
soma = 0
maior = 0
for i in range (5):
    #inicio do bloco
    num = int(input("Informe o valor:"))
    if num > maior:
        maior = num
    soma = soma + num # Acumulador
    # fim do bloco 
print(f" O resultado da soma é {soma} e o maior número digitado é {maior}")