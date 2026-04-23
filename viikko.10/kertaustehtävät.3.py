kirjasto = {
    "moro": ["moro", 1999, "poro"],
    "minä": ["minä", 2005, "draama"],
    "marko": ["marko", 2002, "romaani"]
}

print("Kirjoittaja ja genre:", kirjasto["moro"][0], kirjasto["minä"][2])

kirjasto["marko"][2] = "tietokirja"

kirjasto["meikä"] = ["meikäläinen", 2024, "fantasia"]

del kirjasto["moro"]

print("Päivitetty sanakirja:", kirjasto)