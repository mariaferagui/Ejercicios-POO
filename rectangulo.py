## Ejercicio 10
# Crear una clase Rectángulo, con atributos base y altura.
# Crear también el constructor de la clase y los métodos necesarios para calcular
# el área y el perímetro. Crear otra clase PruebaRectángulo que pruebe varios
# rectángulos y muestre por pantalla sus áreas y perímetros


class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcula_perimetro(self):
        return self.base * 2 + self.altura * 2
    def calcula_area(self):
        return self.base * self.altura
class PruebaRectangulo(Rectangulo):
    def __init__(self,base,altura):
        super().__init__(base,altura)
    rectangulo1 = Rectangulo(1.5,3)
    print (rectangulo1.calcula_perimetro(), rectangulo1.calcula_area())
    rectangulo2 = Rectangulo(4,1)
    print (rectangulo2.calcula_perimetro(), rectangulo2.calcula_area())
    cuadrado = Rectangulo (2,2)
    print (cuadrado.calcula_perimetro(), cuadrado.calcula_area())

PruebaRectangulo(' ',' ' )
