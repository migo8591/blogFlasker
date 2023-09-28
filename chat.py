from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    # Esta es la llave foránea
    books = db.relationship('Book', backref='author', lazy=True)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    
    # Esta es la llave foránea
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
#https://chat.openai.com/share/27e2542b-8b1a-4806-9f0c-58207ce1a293
"""
En SQLAlchemy, `db.ForeignKey` y `db.relationship` son dos conceptos clave para definir las relaciones entre tablas en una base de datos relacional. Ambos se utilizan en el contexto de modelos de datos SQLAlchemy, que son clases de Python que representan tablas de la base de datos. Aquí está la diferencia entre ellos:

1. `db.ForeignKey`:
   - `db.ForeignKey` se utiliza para definir una clave externa en una tabla. Representa una columna en una tabla que hace referencia a la clave primaria de otra tabla.
   - Esta clave externa se utiliza para establecer una relación entre dos tablas. Por ejemplo, si tienes una tabla de "Pedidos" y otra de "Clientes", puedes usar `db.ForeignKey` para crear una relación entre ellas mediante una columna en la tabla "Pedidos" que haga referencia a la clave primaria de la tabla "Clientes".
   - `db.ForeignKey` se define dentro de la clase de modelo como un campo en la tabla que hace referencia a otra tabla y se asocia con un campo específico en esa otra tabla.

Ejemplo de `db.ForeignKey`:
```python
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
```

2. `db.relationship`:
   - `db.relationship` se utiliza para definir una relación entre dos modelos de datos (tablas) en SQLAlchemy. Esta relación define cómo dos tablas están conectadas y cómo se pueden acceder a los datos relacionados.
   - A diferencia de `db.ForeignKey`, que se usa para definir la relación a nivel de base de datos, `db.relationship` se utiliza para definir cómo se acceden y manipulan los datos relacionados a nivel de objeto en Python.
   - Puedes usar `db.relationship` en una clase de modelo para indicar la relación entre dos modelos y especificar cómo SQLAlchemy debe cargar los datos relacionados cuando se consulta la base de datos.

Ejemplo de `db.relationship`:
```python
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)
```

En este ejemplo, `db.relationship` en la clase `Cliente` indica que hay una relación entre la tabla "Cliente" y la tabla "Pedido" a través del campo "pedidos". La opción `backref` permite acceder a los pedidos de un cliente desde un objeto cliente, y la opción `lazy` controla cuándo se cargan los datos relacionados.

En resumen, `db.ForeignKey` se utiliza para definir las claves externas y las relaciones a nivel de base de datos, mientras que `db.relationship` se utiliza para definir cómo se acceden y gestionan las relaciones entre modelos de datos a nivel de objeto en Python. Ambos son esenciales para trabajar con bases de datos relacionales en SQLAlchemy.
"""

