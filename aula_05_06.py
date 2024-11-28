#
gab = ["A","B","B","D","E"]
resp = ["A","B","B","D","E"]
acertos = 0
erros = 0
for i in range(len(resp)):
   if resp [i] == gab [i]: # Condição
      acertos += 1 
   else:
      erros += 1
print(f" A quantidade de acertos são: {acertos}")
print(f" A quantidade de erros são: {erros}")