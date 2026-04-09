vuosi = ("tammikuu","helmikuu","maaliskuu","huhtikuu","toukokuu","kesäkuu","heinäkuu","elokuu","syyskuu","lokakuu","marraskuu","joulukuu")

vuodenaika = ("Kevät", "Kesä", "Syksy","Talvi")

kuukausi = int(input("Anna kuukausi numerolla 1-12"))

kk = vuosi[kuukausi-1]

if kk == 12 or 1 or 2:
    print("Kuukautesi on talvella")
elif kk == 3 or 4 or 5:
    print("Kuukautesi on keväällä")
elif kk == 6 or 7 or 8:
    print("Kuukautesi on kesällä")
else:
    print("Kuukautesi on syksyllä")




