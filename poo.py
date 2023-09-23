"""
Los decoradores de clase son una característica en Python que permite modificar el comportamiento de métodos y propiedades dentro de una clase. Estos decoradores son anotaciones que se colocan justo encima de métodos o propiedades de clase para cambiar su funcionamiento de alguna manera específica. Los decoradores de clase más comunes son @classmethod, @property, y los métodos setter. Aquí te explico qué hace cada uno de ellos:
"""
"""
1.@classmethod:
a)@classmethod es un decorador que se utiliza para definir métodos de clase en una clase. Un método de clase es un método que se puede llamar en la clase misma, en lugar de en una instancia de la clase. Esto significa que puede acceder a los atributos y métodos de la clase en lugar de a los de una instancia.
b)Se utiliza comúnmente para crear métodos de fábrica que generan instancias de la clase o para realizar operaciones relacionadas con la clase en lugar de con instancias individuales.
c)Se define con la firma del método que incluye un primer argumento llamado cls, que hace referencia a la clase misma.
"""
class MiClase:
    valor = 0

    @classmethod
    def incrementar_valor(cls):
        cls.valor += 1

# Uso de un método de clase
MiClase.incrementar_valor()
print(MiClase.valor)  # Imprimirá 1
"""
2. @property:
a) @property es un decorador que se utiliza para definir métodos como propiedades de solo lectura. Esto significa que puedes acceder a la propiedad como si fuera un atributo, pero no puedes asignar un nuevo valor directamente a la propiedad.
b) Se utiliza para encapsular la lógica de acceso a un atributo y para asegurarse de que se realicen acciones específicas cuando se accede a la propiedad.
"""
class MiClase:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

objeto = MiClase(42)
print(objeto.x)  # Acceder a la propiedad x
"""
3.Setter (Método @property_name.setter):
a)Junto con @property, puedes definir un método setter para permitir la asignación de valores a una propiedad. Esto se hace mediante el nombre de la propiedad seguido de .setter.
b) El método setter se ejecuta cuando intentas asignar un valor a la propiedad y te permite realizar validaciones u otras acciones antes de aceptar el valor.
"""
class MiClase:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor < 0:
            raise ValueError("El valor no puede ser negativo")
        self._x = valor

objeto = MiClase(42)
objeto.x = 10  # Asignar un nuevo valor a la propiedad x
"""
En resumen, los decoradores de clase @classmethod, @property, y los métodos setter permiten definir métodos y propiedades con comportamientos específicos en una clase. @classmethod se utiliza para métodos de clase, @property para propiedades de solo lectura y el método setter para permitir la asignación controlada de valores a una propiedad. Estos decoradores ayudan a mejorar la encapsulación y el control en la programación orientada a objetos en Python
"""
myKnowlegde = ["JavaScript", "Python",  "React", "Flask", "Express", "Node","CSS", "HTML"] 
noSonLenguajes = myKnowlegde[6:8]
dontLenguages= myKnowlegde[6:]
sonLenguajes = myKnowlegde[0:2]
entiendo =myKnowlegde[:2]
frameworks=myKnowlegde[2:5]
saltos=myKnowlegde[0:5:2]
test=myKnowlegde[::-2]
print(noSonLenguajes, dontLenguages)
print(sonLenguajes, entiendo)
print(frameworks)
print(saltos)
print(test)
myKnowlegde.insert(9, "SQL Server")
myKnowlegde.append("SQLAlchemy")
myKnowlegde.append("MySQL")
myKnowlegde.insert(0,"Git")
print(f"Tecnologias que conozco: {len(myKnowlegde)}, {myKnowlegde}")
print(myKnowlegde)
myKnowlegde.remove("SQL Server")
# print(f"Tecnologias que conozco: {len(myKnowlegde)}, {for x in myKnowlegde: x}")
def myConocimiento():
    for x in myKnowlegde:
        print(x, end=" ",sep=",")
myConocimiento()
calificacion = 10
color = 'verde' if calificacion >=7 else 'rojo'
print()
print(calificacion, color) 
#https://github.com/codigofacilito/curso-profesional-python/blob/master/8.-Clases/metodos.py


#freeCamp
#https://youtu.be/DLikpfc64cA