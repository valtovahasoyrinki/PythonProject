import math
luku=int(input("Sano joku luku"))
while True:
    if luku < 0:
        print ("Virheellinen numero")
        break
    elif luku > 0:
        print (f"luvun {luku} neliöjuuri on: {math.sqrt(luku)}.")
        break
print("Exiting...")
