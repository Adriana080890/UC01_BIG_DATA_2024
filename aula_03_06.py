# 3 numeros inteiros, descobrir o maior
n1 = int(input('Informe o primeiro numero:'))
n2 = int(input('Informe o segundo numero:'))
n3 = int(input('Informe o terceiro numero:'))
if (n1>n2) and (n1>n3):
    print(f'{n1} é o maior valor')
elif (n2>n1) and (n2>n3):
    print(f'{n2} é o maior valor') 
else:
    print(f'{n3} é o maior valor') 