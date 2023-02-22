print("------------------------------------------")
print("--------MAYOR DE 2 NUMEROS ENTEROS:-------")
print("------------------------------------------")


# input

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

#processing
if x == y:
    # output
    print(" los numeros son iguales....")
    mayor = x
else:
    if x > y:
        mayor = x
    else:
        mayor = y 
    
# output
print("------------------------------------------")
print("----------EL NUMERO MAYO ES --------------")
print("------------------------------------------")

print("TOTAL A PAGAR DE LA LLAMADA: " + str(x) + " y " + str (y) + " es " + str(mayor))