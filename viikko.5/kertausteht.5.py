import math

while True:

        lasku=input("Valitse yhteenlasku, vähennyslasku, kertolasku tai jakolasku.")
        luku1=float(input("Anna ensimmäinen luku:"))
        luku2=float(input("Anna toinen luku:"))


        if lasku == "yhteenlasku":
            print (luku1+luku2)

        elif lasku == "vähennyslasku":
            print (luku1-luku2)

        elif lasku == "kertolasku":
            print (luku1*luku2)
        elif lasku == "jakolasku":
            print (luku1/luku2)
        elif lasku == "lopetus":
            break





