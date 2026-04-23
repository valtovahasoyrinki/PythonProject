import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print("Anna ensimmäisen pisteen koordinaatit:")
x1 = float(input("Sano x1: "))
y1 = float(input("Sano y1: "))
piste1 = create_point(x1, y1)

print("Anna toisen pisteen koordinaatit:")
x2 = float(input("Sano x2: "))
y2 = float(input("Sano y2: "))
piste2 = create_point(x2, y2)

etaisyys = distance(piste1, piste2)

print("Pisteiden väli on :", etaisyys)