 
# Definir una función que eleve al cuadrado un número
def cuadrado(x):
    return x * x

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Utilizar la función map para aplicar la función cuadrado a cada elemento de la lista
resultado = list(map(cuadrado, numeros))

# Imprimir el resultado
print(resultado)
"""
Cuando escribes un programa en Python utilizando ciclos, estás utilizando programación estructurada. La programación estructurada es un enfoque de programación que se basa en la idea de dividir un programa en estructuras de control más pequeñas y manejables, como ciclos y estructuras condicionales, para resolver problemas de manera más organizada y eficiente.

En Python, los ciclos pueden implementarse utilizando las instrucciones for y while. Estos ciclos te permiten repetir una serie de instrucciones un número específico de veces (en el caso de for) o mientras se cumpla una condición específica (en el caso de while).

Ejemplo de un ciclo for en Python:

python
Copy code
for i in range(5):
    print(i)
Este código imprimirá los números del 0 al 4 en la consola.

Ejemplo de un ciclo while en Python:

python
Copy code
contador = 0
while contador < 5:
    print(contador)
    contador += 1
Este código también imprimirá los números del 0 al 4 en la consola mientras la condición contador < 5 sea verdadera.

La programación estructurada se centra en la organización y la lógica del programa a través de estructuras de control como ciclos y condicionales, lo que facilita la comprensión y el mantenimiento del código. Python, como lenguaje de programación, es adecuado tanto para la programación estructurada como para otros paradigmas de programación, como la programación orientada a objetos y la programación funcional.

Por supuesto, aquí tienes un ejemplo de programación en Python utilizando programación funcional. En la programación funcional, se enfatiza el uso de funciones puras y la inmutabilidad de los datos. Un concepto importante en la programación funcional es el de las funciones de orden superior, que son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultado. Un ejemplo común de esto en Python es el uso de las funciones map, filter y reduce. Aquí tienes un ejemplo de uso de map para aplicar una función a una lista de números:

Este código aplicará la función cuadrado a cada elemento de la lista numeros utilizando la función map y devolverá una nueva lista con los resultados. El resultado será [1, 4, 9, 16, 25], ya que cada número se elevará al cuadrado.

Este es solo un ejemplo simple de programación funcional en Python. La programación funcional también incluye conceptos como la recursión, el uso de funciones anónimas (lambda), y la aplicación de funciones como filter y reduce para filtrar y reducir datos, respectivamente. Estos conceptos se utilizan para escribir código más conciso y expresivo, y promueven un estilo de programación más declarativo.
"""
"""
Si pudiera retroceder el tiempo, cambiaría todo aquello que no es puro por cosas verdaderas. Como formarme mejor para ser más atractivo a una potencial esposa. Sin embargo, pienso que nunca fue mi destino estar con alguien. No aproveché las escasas oportunidades, y cuando decidí buscar, no encontre.


I could come back time, I change all that it's not pure for true things. Like I take advantage my time in study. Nevertheless, I think, I never was my destine to be with a girl. I didn't take advantage the few opportunities and when I decided to look for somebody I didn't find out.

"If I could turn back time, I would change everything that isn't pure for genuine things. Like improving myself to be more attractive to a potential spouse. However, I believe it was never my destiny to be with someone. I didn't seize the scarce opportunities, and when I decided to look, I didn't find."

"If I could come back in time, I would change everything that is not pure for genuine things. Like investing my time in studying. Nevertheless, I think it was never my destiny to be with a girl. I didn't seize the few opportunities, and when I decided to look for somebody, I didn't find anyone."
"""