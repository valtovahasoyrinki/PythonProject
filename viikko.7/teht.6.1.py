import random

def heitto():
    tulos = random.randint(1,6)
    return tulos

saatu_luku = 0

while saatu_luku != 6:
    saatu_luku = heitto()
    print (saatu_luku)
