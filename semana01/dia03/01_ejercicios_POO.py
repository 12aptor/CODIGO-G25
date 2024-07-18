"""Crear un programa que simule el funcionamiento de un cajero automático.
Deberá tener un menú con las siguientes opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar saldo disponible
Iniciar con un saldo de $1000."""

class Cajero:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def consultar_saldo(self):
        print(f"Saldo disponible: ${self.saldo}")

    def depositar_dinero(self, monto: float) -> None:
        if monto <= 0:
            print("Cantidad no válida")
            return
        self.saldo += monto
        print(f"Depósito realizado. Saldo actual: ${self.saldo}")

    def retirar_dinero(self, monto: float) -> None:
        if monto <= 0:
            print("Cantidad no válida")
            return
        
        if monto > self.saldo:
            print("Saldo insuficiente")
            return
        
        self.saldo -= monto
        print(f"Retiro realizado. Saldo actual: ${self.saldo}")

def main():
    cajero = Cajero(1000)

    while True:
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = int(input("\nOpción: "))

        if opcion > 4:
            print("Opción no válida")
            # Continue sirve para que el programa no se detenga y vuelva a ejecutar el ciclo
            continue

        if opcion == 1:
            # Consultar el saldo
            cajero.consultar_saldo()
        elif opcion == 2:
            # Depositar dinero
            monto = float(input("Cuánto desea depositar: "))
            cajero.depositar_dinero(monto)
        elif opcion == 3:
            # Retirar dinero
            monto = float(input("Cuánto desea retirar: "))
            cajero.retirar_dinero(monto)
        elif opcion == 4:
            # Salir
            print("Gracias por visitarnos")
            break
        
main()