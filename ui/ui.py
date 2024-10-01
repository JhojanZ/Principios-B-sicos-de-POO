from cuenta.banco import Banco

banco = Banco()

def mostrar_menu():
    print("")
    print("------------------------------")
    print("         Opciones:")
    print("1. Crear nueva cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar datos de la cuenta")
    print("5. Mostrar todas las cuentas")
    print("6. Salir")

def crear_cuenta():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    documento_identidad = int(input("Ingrese el documento de identidad: "))
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))

    banco.agregar_cuenta(numero_cuenta, documento_identidad, nombre_cliente, saldo_inicial)

def depositar_dinero():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    banco.depositar_banco(numero_cuenta, cantidad)

def retirar_dinero():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    banco.retirar_banco(numero_cuenta, cantidad)

def mostrar_cuenta():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    banco.mostrar_datos(numero_cuenta)

def mostrar_todas_las_cuentas():
    banco.mostrar_todo()
