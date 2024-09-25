import random
import string

def arrSum(arr):
    w = 0
    for e in arr:
        w += e
    return str(w)

polecenie = input()
iloscKostek = int(polecenie[polecenie.index("d")-1])
rodzajKostek = int(polecenie[polecenie.index("d")+1])
kostki = []

for i in range(iloscKostek):
    kostki.append(random.randint(1 , rodzajKostek))

print(*kostki, sep = ' + ' + ' = '+arrSum(kostki))