lentoasema = {}

while True:
    tulos = int(input("Haluatko lisätä uuden lentoaseman? (1), Hakea jo syötetyn lentoaseman? (2), Lopettaa? (3): Vastaa numerolla: "))

    if tulos == 3:
        print("Näkemiin!!")
        break
    elif tulos == 1:
        icao = input("Syötä aseman icao tunnus: ")
        nimi = input("Anna lentokentän nimi: ")

        lentoasema[icao] = nimi
        print("Lentoasema tallennettu")
    elif tulos == 2:
        icao = input("Syötä haettavan lentoaseman icao tunnus: ")
        if icao in lentoasema:
            print(f"Lentoaseman nimi on: {lentoasema[icao]}")
        else:
            print("Tuntematon lentoasemakoodi.")

