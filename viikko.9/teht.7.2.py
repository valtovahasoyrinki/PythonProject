nimet = set()

while True:
    n = input ("Anna nimi:")
    if n == "":
        break

    if n in nimet:
            print("Nimi on jo syötetty aiemmin")
    else:
        print("Nimi on uusi")
        nimet.add(n)















