import random

def heitto(tahkot):
    tulos = random.randint(1, tahkot)
    return tulos

maksimi = int(input("Kuinka monta tahkoa nopassa on? "))

saatu_luku = 0

while saatu_luku != maksimi:
    saatu_luku = heitto(maksimi)
    print(f"Heitit: {saatu_luku}")