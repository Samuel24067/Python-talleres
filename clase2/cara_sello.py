import random
resultado=(random.randint(1, 2))


if resultado==1:
    print("Has sacado Cara")
if resultado==2:
    print("Has sacado sello")

opcion=int(input("Elija el lado de la moneda: cara = 1, sello = 2: "))

print("Sacaste: ", resultado)

if opcion==resultado:
    print("ganaste")
else:
    print("perdiste")