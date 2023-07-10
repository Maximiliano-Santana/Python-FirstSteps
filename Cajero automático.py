from this import d
from tkinter.filedialog import SaveFileDialog

accion = ""
cuenta = 1000

print("Bienvenido al cajero automático\n¿Qué acción desea realizar?\n\na)Ingresar dinero a la cuenta \nb)Retirar dinero a la cuenta \nc)Mostrar dinero disponible \nd)Salir\n")

while accion != 'd':
    
    accion = (input("Acción que desea realizar: ")).lower()

    if accion == 'a':
        operacion = float(input("Saldo que desea ingresar: "))
        cuenta += operacion
        print(f"El saldo final es {cuenta:.2f}")
    elif accion == 'b':
        operacion = float(input("Saldo que desea Retirar: "))
        cuenta -= operacion
        print(f"Saldo final es de {cuenta:.2f}")
    elif accion == 'c':
        print(f"Saldo: {cuenta}")
    elif accion == 'd':
        print("Usted Salió")
    else:
        print("Accion invalida, intente de nuevo")