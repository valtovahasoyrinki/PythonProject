lista = []

while True:
    arvo = int(input("Uusi arvo:"))

    if arvo == 0:
        print("Heippa!")

    lista.append(arvo)
    print("Lista nyt", lista)
    print("Lista järjestettynä", sorted(lista))