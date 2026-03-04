import math
nimi=input("kerro nimesi.")
if nimi=="Matti":
    print("Seuraava, kiitos")
else:
    keitot=int(input("Kuinka monta keittoannosta"))
    print(f"Kokonaishinta on {keitot*5.9}€.")
