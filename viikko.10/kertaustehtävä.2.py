oppilaat = {
    "oliver" : ["oliver", 3, "insinöörimatikka"],
    "saulus" : ["saulus", 7, "kotitalous"],
    "marko" : ["marko", 6, "äidinkieli"]
}
print (oppilaat["oliver"][0], oppilaat["saulus"][2])
oppilaat["marko"][2] = "liikunta"

del oppilaat["oliver"]

print (oppilaat)
