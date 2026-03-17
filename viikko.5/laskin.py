print("\n-----------------TERVETULOA KÄYTTÄMÄÄN LASKINTA---------------")

while True:
    print("\nValitse mitä toimintoa haluat käyttää: \n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku \n D: Jakolasku")
    valinta = input("Valintasi (A-D, Q lopettaa):").upper()


    if valinta == "Q":
        print("Ohjelma päättyy")
        break

    a=float(input("anna eka luku"))
    b=float(input("anna toka luku"))

    if valinta == "A":
        print ("Lukujen summa on,")


