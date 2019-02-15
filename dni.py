## Ejercicio 8
# Crea una clase NIF. Los atributos serán el número de DNI y la letra.
# La clase contendrá un método que calcule la letra del NIF a partir del número de DNI. 

class Nif():
    def __init__(self, NIF_number, NIF_letter = None):
        self.NIF_number = NIF_number
        self.NIF_letter = NIF_letter
    def calcula_letra(self,):
        posibles_letras = {0:'T',1:'R',2:'W',3:'A',4:'G',5:'M',6:'Y',7:'F',8:'P',9:'D',10:'X',11:'B',12:'N',13:'J',14:'Z',15:'S',16:'Q',17:'V',18:'H',19:'L',20:'C',21:'K',22:'E'}
        resto = self.NIF_number % 23
        letra = posibles_letras[resto]
        print ('La letra que le corresponde es: ')
        return letra

DNI = Nif(51495003,'G')
print (DNI.calcula_letra())

repetir = True

while repetir:
    DNI_numero = input ('Introduzca su número del DNI: ')
    if len(DNI_numero)!= 8:
        repetir = True
    try:
        DNI_numero = int(DNI_numero)
        repetir = False
    except ValueError:
        repetir = True


DNI = Nif(DNI_numero,)
print (DNI.calcula_letra())
