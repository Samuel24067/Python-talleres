PiensaenUnnumero=("Piensa en un numero ")
print(PiensaenUnnumero)
sumale5=("Sumale 5 al numero")
print(sumale5)
x3=("multiplicalo por 3")
print(x3)
restar15=("Por ultimo restale 15")
print(restar15)
numeroM=int(input("Ingrese el resultado:"))
resultado=(numeroM/3)
print(resultado)

resultadofinal=input("Es correcto? \n Digite s o n \n")

if resultadofinal == "s":
    print("Soy todo un adivino")
elif resultadofinal=="n":
    print("Rectifica las cuentas mi bro")
else:
    print("Rectifica las cuentas")

