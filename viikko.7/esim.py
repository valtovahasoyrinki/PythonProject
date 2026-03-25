def neliosumma (a, b):
    _tulos = a**2 +b**2
    return _tulos

luku1 = float(input("Anna eka luku: "))
luku2 = float(input("Anna toka luku: "))
tulos = neliosumma(luku1, luku2)

print (f"lukujen {luku1} ja {luku2} neliösumma on {tulos}")



def inventaario (tavarat):
    print ("Sinulla on seuraavat tavarat repussa:")
    for t in tavarat:
        print( "-" + t)
    tavarat.clear()
    return

reppu = ["taskulamppu", "otsalamppu", "pöytälamppu"]
inventaario(reppu)
reppu.append("Eväsleipä")

inventaario(reppu)

