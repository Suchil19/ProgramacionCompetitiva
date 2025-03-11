# Curso de Funciones en Python

## Índice
1. [Introducción a las Funciones](#introducción-a-las-funciones)
2. [Definiendo Funciones](#definiendo-funciones)
3. [Parámetros y Argumentos](#parámetros-y-argumentos)
4. [Valores de Retorno](#valores-de-retorno)
5. [Funciones Anidadas](#funciones-anidadas)
6. [Funciones Lambda](#funciones-lambda)
7. [Ejercicios](#ejercicios)

## Introducción a las Funciones
Las funciones son bloques de código reutilizables que realizan una tarea específica. Ayudan a organizar y estructurar el código, haciéndolo más legible y fácil de mantener.

```python
# Ejemplo de una función simple
def saludar():
    print("¡Hola, Mundo!")

saludar()# Llama a la función
```

## Definiendo Funciones

Para definir una función en Python, se utiliza la palabra clave `def` seguida del nombre de la función y paréntesis. El código dentro de la función se escribe con sangría.

```python
def nombre_funcion():
    # Código de la función
```


## Parámetros y Argumentos

Las funciones pueden aceptar parámetros que permiten pasar información a la función.

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")
```

## `def saludar(nombre):`

- `def`: Esta palabra clave se utiliza para definir una función en Python.

- `saludar`: Este es el nombre de la función. Puedes nombrar a una función como quieras, siempre que sigas las reglas de nomenclatura de Python.

- `nombre`: Este es un parámetro de la función. Un parámetro es una variable en una definición de función que recibe un valor cuando la función es llamada. En este caso, `nombre` es el parámetro que representará el nombre de la persona a saludar.

- `:`: Los dos puntos indican el final de la definición de la cabecera de la función y el comienzo del bloque de código que define lo que hace la función.

## `print(f"¡Hola, {nombre}!")`

- `print`: Esta es una función incorporada en Python que se utiliza para imprimir mensajes en la pantalla.

- `f"¡Hola, {nombre}!"`: Esto es una cadena de texto formateada (f-string). Las f-strings permiten incrustar expresiones dentro de las llaves `{}` que serán evaluadas en tiempo de ejecución y luego formateadas como una cadena.

  - `"¡Hola, "`: Es una cadena literal que será impresa tal cual.

  - `{nombre}`: Esto es una expresión dentro de la f-string. Cuando se llame a la función `saludar`, el valor pasado al parámetro `nombre` será insertado en este lugar dentro de la cadena.


saludar("Luis")  # Llama a la función con el argumento 'Luis'

## Valores de Retorno

- Las funciones pueden devolver valores utilizando la palabra clave return.

```python
def sumar(a, b):
    return a + b
```
resultado = sumar(3, 4)
print(resultado)  # Imprime 7


## Funciones Anidadas

Una función puede ser definida dentro de otra función.

```python
def exterior():
    def interior():
        print("Dentro de la función interior")
    interior()
# Llama a la función exterior, que a su vez llama a la función interior
exterior() 

