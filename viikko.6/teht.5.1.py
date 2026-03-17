import random

maara=int(input("Montako noppaa heitetään?"))

summa = 0
for noppa in range(maara):
    heitto = random.randint(1, 6)
    print(heitto)
    summa += heitto

print ("Summaksi tuli", summa)

