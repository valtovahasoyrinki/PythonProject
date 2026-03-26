lista = ["Marko", "Joonas", "Aleksi", "Mauri", "kahvikuppi", "Antero"]

laskuri = 0
for lista in lista:
    if len(lista) > 5:
        laskuri += 1

print ("Yli 5 kirjaimen sanoja on", laskuri)