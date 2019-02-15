## Ejercicio 1

# Crea una clase Cuenta con los métodos ingreso, reintegro y transferencia.
# La clase contendrá un constructor por defecto, un constructor con parámetros,
# y los métodos para obtener información (los también llamados getters.
# Suelen tener la forma get_xxxxx)o para almacenar información
#(también llamados setters. Tienen la forma de set_xxxx)


class Cuenta():
    def __init__(self, saldo):
        self.saldo = saldo
    def ingreso(self, ingreso):
        self.ingreso = ingreso
        self.saldo += self.ingreso
    def reintegro(self, reintegro):
        self.reintegro = reintegro
        self.saldo -= self.reintegro
    def transferencia_favor(self, transferencia_favor):        #Me mandan dinero
        self.transferencia_favor = transferencia_favor
        self.saldo += self.transferencia_favor
    def transferencia_contra(self, transferencia_contra):        #Mando dinero
        self.transferencia_contra = transferencia_contra
        self.saldo -= self.transferencia_contra
    def dime_saldo(self):
        return self.saldo

cuenta1 = Cuenta(1300)
cuenta1.reintegro(100)
print (cuenta1.dime_saldo())

cuenta2 = Cuenta(int(input('Introduzca el saldo inicial de la cuenta: ')))
cuenta2.transferencia_favor(int(input('Introduzca la cantidad de transferencia a favor: ')))
cuenta2.reintegro(int(input('Introduzca la cantidad de reintegro: ')))
print (cuenta2.dime_saldo())
