## Ejercicio 2
# Crea una clase Contador con los métodos para incrementar y decrementar el contador.
# La clase contendrá un constructor por defecto, un constructor con parámetros y los métodos getters y setters

class Contador():
    def __init__(self,n,x):
        self.n = n  #Número inicial
        self.x = x  #Número que sumaremos o restaremos
    def sube(self):
        self.n += self.x
        #return self.n += self.x
    def baja(self):
        self.n -= self.x
        #return self.n -= self.x
    def dame_valor(self):
        return self.n


numero = float (input('Introduzca un número: '))
incremento = float (input ('Introduzca el incremento: '))
contador = Contador(numero,incremento)
contador.baja()
print (contador.dame_valor()) #contador.n devuelve lo mismo
