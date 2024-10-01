from cuenta.cuenta import Cuenta

class Banco:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, numero_cuenta, documento_identidad, nombre_cliente, saldo_inicial):
        nueva_cuenta = Cuenta(numero_cuenta, documento_identidad, nombre_cliente, saldo_inicial)
        self.cuentas[numero_cuenta] = nueva_cuenta
        print("Cuenta creada exitosamente.")

    def depositar_banco(self, numero_cuenta, cantidad):
        cuenta = self.cuentas.get(numero_cuenta)
        if cuenta:
            cuenta.guardar_dinero(cantidad)  
            print("Depósito realizado con éxito.")
        else:
            print("Cuenta no encontrada.")

    def retirar_banco(self, numero_cuenta, cantidad):
        cuenta = self.cuentas.get(numero_cuenta)
        if cuenta:
            if cuenta.retirar_dinero(cantidad):  
                print("Retiro realizado con éxito.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Cuenta no encontrada.")

    def mostrar_datos(self, numero_cuenta):
        cuenta = self.cuentas.get(numero_cuenta)
        if cuenta:
            cuenta.mostrar_datos() 
        else:
            print("Cuenta no encontrada.")

    def mostrar_todo(self):
        if not self.cuentas:
            print("No hay cuentas registradas.")

        for cuenta in self.cuentas.values():
            cuenta.mostrar_datos()  
