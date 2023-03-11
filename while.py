
pInicial=100000
registrar="r"
contador = 0
gastos=0

while (registrar=="r" or registrar=="R") and contador<3 and pInicial>=gastos:          
        precio=int(input("Ingrese el valor del producto: \n"))
        print("su gasto fue de: ", precio)
        pInicial=pInicial-precio
        gastos = gastos+precio        
        contador =contador+1
        print("Le queda: ", pInicial)
        if contador<3:
            registrar=input("para registrar otro gasto r/R para salir n/N: ")
        
        
print("__________________")
print("el saldo de su presupuesto es: ", pInicial)
print("sus gastos totales fueron: ", gastos)
        
