print("------------------------------------------")
print("--------MAYOR DE 2 NUMEROS ENTEROS:-------")
print("------------------------------------------")


# input

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

#processing
if x == y:
    print(" los numeros son iguales: ....")
else:
    if x>y:
        mayor = x
    else:
        mayor = y 
        # Output
print("EL MAYOR ENTRE " + str(x) + " y " + str (y) + " es " + str(mayor))

    

