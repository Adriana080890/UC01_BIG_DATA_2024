# Exercicio 2
qtd_par = 0
qtd_impar = 0
num = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(num)):
   if num [i] % 2 == 0: # Condição
      qtd_par += 1 
   else:
      qtd_impar +=1
print(f" A quantidade de números pares são: {qtd_par}")
print(f" A quantidade de números ímpares são: {qtd_impar}")
print(" A ordem de criação")
print(num)
print(" A ordem reversa")
num.reverse()
print(num)
print(" A ordem de crescente")
num.sort() #Crescente sorte / reverse=true - Decrescente
print(num)