cont=0
total=0
for i in range(1,6,1):
    price=int(input("Ingrese el valor del producto \n"))
    cantidad=int(input("Ingrese la cantidad del producto"))
    cont=cont+1
    subtotal=price*cantidad 
    total=total+subtotal
    
    

print("Se registraron",cont ,"Referencias")

print("El total a pagar es: ", total)

billete=int(input("Ingrese el valor del billete con el que pagara: "))
cambio=billete-total

print("su cambio es: ", cambio)

minutos=input("Ya tienes moil exito?")
if(minutos=="si"):
    print("Obtuvo: ", cont, "minutos")
else:
    ("Cambiate para obtener mas beneficios")