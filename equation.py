import math
a = int(input("Saisir a: "))
while a == 0:
    print("doit être différent de 0")
    a = int(input("Saisir a: "))

b = int(input("Saisir b: "))
c = int(input("Saisir c: "))

delta = b*b - 4*a*c

print("Delta =", delta)

if delta < 0:
    print("Aucune solution réelle")

elif delta == 0:
    x = -b / (2*a)
    print("Une seule solution:", x)

else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("Deux solutions:")
    print("x1 =", x1)
    print("x2 =", x2)
