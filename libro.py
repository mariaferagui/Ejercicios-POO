## Ejercicio 3
# Crea una clase Libro con los métodos préstamo, devolución y dame_info.
# La clase contendrá un constructor por defecto, un constructor con parámetros
# y los métodos getters y settersque consideres oportunos.

class Libro():
    def __init__(self, name, author, publisher):
        self.name = name
        self.author = author
        self.publisher = publisher
    def dame_info(self):
        print ('El nombre del libro es', self.name , 'el autor es', self.author, 'y la editorial', self.publisher)
        return ' '
    def prestamo(self, date):
        self.date = date
        print ('Si se lleva este ejemplar hoy,', self.date, ', tiene 30 días para devolverlo')
        return ' '
    def devolucion(self, date):
        self.date = date
        print ('Debe devolver este ejemplar antes de la fecha: ', self.date )
        return ' '

don_quijote = Libro ('Don Quijote de La Mancha','Miguel de Cervantes', 'Vicens Vives')
print (don_quijote.dame_info())

cien_años = Libro ('Cien años de Soledad', 'Gabriel García Márquez', 'Santillana')
import time
fecha = time.strftime("%d/%m/%y")   #Fecha actual
print (cien_años.prestamo(fecha))

crimen_castigo = Libro ('Crimen y castigo', 'Fiódor Dostoievski', 'Alianza Editorial')
print (crimen_castigo.devolucion('22/03/2019'))
