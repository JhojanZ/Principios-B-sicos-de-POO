class Cuenta:
    def __init__(self, numero_cuenta, documento_identidad, nombre_cliente, saldo):
        self.numero_cueta = numero_cuenta
        self.documento_identidad = documento_identidad
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo
        self.RETENCION = 0.19

    def guardar_dinero(self, cantidad):
        self.saldo += (cantidad - self.calcular_retencion(cantidad))

    def calcular_retencion(self, cantidad):
        return cantidad * self.RETENCION

    def retirar_dinero(self, cantidad):
        if self.hay_dinero(cantidad):
            self.saldo -= cantidad
            return True
        return False

    def hay_dinero(self, cantidad):
        return self.saldo >= cantidad

    def mostrar_datos(self):
        print( "___________________________________________________")
        print(f"Número de cuenta: {self.numero_cueta}")
        print(f"Documento de identidad: {self.documento_identidad}")
        print(f"Nombre del cliente: {self.nombre_cliente}")
        print(f"Saldo actual: {self.saldo}")
        print("")
