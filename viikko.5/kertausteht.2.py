palkka=float(input("Kuinka paljon on tuntipalkkasi?"))
tunnit=int(input("Kuinka paljon teit tunteja?"))
paiva=input("Mikä viikonpäivä on?")

if paiva == "sunnuntai":
    print(f"Tuntipalkka:{palkka}")
    print(f"Tehdyt tunnit:{tunnit}")
    print(f"Viikonpäivä: {paiva}")
    print(f"Päiväpalkka: {palkka*2*tunnit}")
else:
    print(f"Tuntipalkka:{palkka}")
    print(f"Tehdyt tunnit:{tunnit}")
    print(f"Viikonpäivä: {paiva}")
    print(f"Päiväpalkka: {palkka * tunnit}")
