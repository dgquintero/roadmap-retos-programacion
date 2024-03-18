"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.make_sound()
cat.make_sound()


class Empleado:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Gerente(Empleado):
    def __init__(self, id, name, area):
        super().__init__(id, name)
        self.area = area

class GerenteProyecto(Empleado):
    def __init__(self, id, name, proyecto):
        super().__init__(id, name)
        self.proyecto = proyecto

class Programador(Empleado):
    def __init__(self, id, name, lenguaje):
        super().__init__(id, name)
        self.lenguaje = lenguaje

gerente = Gerente(1, "Juan", "Finanzas")
gerente_proyecto = GerenteProyecto(2, "Maria", "Proyecto 1")
programador = Programador(3, "Pedro", "Python")

print(gerente.area)
print(gerente_proyecto.proyecto)
print(programador.lenguaje)



