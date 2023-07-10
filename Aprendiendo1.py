letra = input("Ingrese caracter de la operación que desea realizar: ").lower()

if letra=='s':
    a = float(input("Inserte el valor de a: "))
    b = float(input("Inserte el valor de b: "))
    resultado = a + b
    print(f"Tu resultado es {resultado:.2f}")
elif letra=='r':
    a = float(input("Inserte el valor de a: "))
    b = float(input("Inserte el valor de b: "))
    resultado = a - b
    print(f"Tu resultado es {resultado:.2f}")
elif letra =='m':
    a = float(input("Inserte el valor de a: "))
    b = float(input("Inserte el valor de b: "))
    resultado = a * b
    print(f"Tu resultado es {resultado:.2f}")
elif letra =='d':
    a = float(input("Inserte el valor de a: "))
    b = float(input("Inserte el valor de b: "))
    resultado = a / b
    print(f"Tu resultado es {resultado:.2f}")
else:
    print("Ese caracter no es valido")