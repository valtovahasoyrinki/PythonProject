suurin= None
pienin= None

while True:
    luku =(input("Sano luku."))
    if luku == "":
        break
    luku=int(luku)

    if suurin is None or luku > suurin:
        suurin=luku
    if pienin is None or luku < pienin:
        pienin=luku

print("Silmukka loppui")

if pienin != None:
    print (f"Pienin luku on {pienin}")
if suurin != None:
    print (f"Suurin luku on {suurin}")
else:
    print ("Syötä luku.")

