num1 = int(input("Primer cifra "))
operacion = int(input("¿Qué operación se va a realizar? Escoge:\n1 para Suma\n2 para resta \n3 para multiplicación \n4 para división\n"))
num2 = int(input("Sgunda cifra "))


if operacion == 1:
    print(num1+num2)
elif operacion == 2:
    print(num1-num2)
elif operacion == 3:
    print(num1*num2)
elif operacion == 4:
    print(num1/num2)


