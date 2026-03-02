import random
luku=random.randint(1,10)
print("Arvaa luku 1-10.")

while True:
    arvaus=int(input("Anna arvauksesi:"))
    if arvaus > luku:
        print ("Arvauksesi on liian suuri.")
    elif arvaus < luku:
        print ("Arvauksesi on liian pieni.")
    else:
        print ("Arvauksesi meni oikein.")
        break