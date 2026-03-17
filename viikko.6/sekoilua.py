nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(nimet)
print(len(nimet))
nimet.append("Matti")
nimet.remove("Pekka")
nimet.insert(3, "Tiina" )

nimet2 = ["Allu", "Ninni"]
nimet.extend(nimet2)
print(nimet)

print(nimet.index("Allu"))

if "Matti" in nimet:
    print("Matti löytyi")
else:
    "Mattia ei löytynyt"


nimet.sort()
print(nimet)

luvut= [2,54,5,6,9,3,]
luvut.sort(reverse=True)
print(luvut)

