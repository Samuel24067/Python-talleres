edad=int(input("Ingresa tu edad \n"))
if 0<=edad<=4:
    print("El cliente entra gratis")
elif 4>edad<=18:
    print("Debera pagar 20 mil")
elif 18<=edad<=60:
    print("Debera pagar 15 mil")
elif 60>edad:
    print("Debera pagar 3 mil")
else:
    print("Ingrese una edad valida")
    

# "<" = menor ">"mayor