leiviskat=float(input("Anna leiviskat"))
naulat=float(input("Anna naulat"))
luodit=float(input("Anna luodit"))

luoti_grammoina=13.3
naula_luoteina=32
leiviska_nauloina=20

kokonais_luodit = (leiviskat*leiviska_nauloina*naula_luoteina) + (naulat*naula_luoteina)+luodit
kokonais_grammat=kokonais_luodit*luoti_grammoina

kilogrammat=int(kokonais_grammat//1000)
grammat=kokonais_grammat%1000

print ("Massa on:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")



