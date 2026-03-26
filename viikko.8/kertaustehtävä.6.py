def summa (a, b):
    return a + b
def erotus (a, b):
    return a - b
def tulo (a, b):
    return a * b
def jako (a, b):
    if b != 0:
        return a / b
    else:
        return "Ei voi jakaa nollalla"

l1 = float(input("anna ensimmäinen luku"))
l2 = float(input("anna tonen luku"))

print("summa", summa(l1, l2))
print("erotus", erotus(l1, l2))
print("tulo", tulo(l1, l2))
print("jako", jako(l1, l2))
