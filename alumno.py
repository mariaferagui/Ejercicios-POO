## Ejercicio 11
#Se conoce de un alumno: número de matrícula, nombre y tres notas parciales (nota1, nota2, nota3).
# El programa debe imprimir: la matrícula, nombre, nota final e indique con un mensaje
# si el alumno aprobó (nota final >= 4,8) o no aprobó (nota final < 4,8) la asignatura.

class Alumno():
    def __init__(self,ID_number, name, nota1, nota2, nota3):
        self.ID_number = ID_number
        self.name = name
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def dime_matricula(self):
        print ('El número de matrícula es: ')
        return self.ID_number
    def dime_nombre(self):
        print ('El nombre del alumno es: ')
        return self.name
    def calcula_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        self.media = media
        return self.media
    def dime_aprobado(self):
        print ('Su nota media es: ', Alumno.calcula_media(self))
        if self.media>=4.8:
            return '¡Felicidades! Ha aprobado'
        else:
            return 'Lo siento, ha suspendido'

alumno1 = Alumno(15673, 'Carlos', 7, 5, 4)
print (alumno1.dime_matricula(), alumno1.calcula_media())

alumno2 = Alumno(1648,'Ainhoa',3,7.5,8)
print (alumno2.dime_nombre(), alumno2.dime_aprobado())

alumno3 = Alumno(12345, 'Lucia',3,4.5,5)
print (alumno3.dime_aprobado())
