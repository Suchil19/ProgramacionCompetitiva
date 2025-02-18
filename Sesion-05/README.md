# Bucle For en Python

A continuación explicaremos el bucle `for` y sus particularidades en Python, que comparado con otros lenguajes de programación, tiene ciertas diferencias.

## Introducción al Bucle For

El `for` es un tipo de bucle, parecido al `while` pero con ciertas diferencias. La principal es que el número de iteraciones de un `for` está definido de antemano, mientras que en un `while` no. La diferencia principal con respecto al `while` es en la condición. Mientras que en el `while` la condición era evaluada en cada iteración para decidir si volver a ejecutar o no el código, en el `for` no existe tal condición, sino un iterable que define las veces que se ejecutará el código.

### Ejemplo Básico

- En el siguiente ejemplo vemos un bucle `for` que se ejecuta 5 veces, y donde la `i` incrementa su valor automáticamente en 1 en cada iteración.

```python
for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
```

- En Python, se puede iterar prácticamente cualquier cosa, como cadenas, listas, tuplas y diccionarios. Por ejemplo, al iterar una cadena, cada letra será un elemento del bucle.

## Ejemplo Cadena

```python
for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n
```

- Para entender al cien por cien los bucles for, y cómo Python fue diseñado como lenguaje de programación, es muy importante entender los conceptos de iterables e iteradores.

## Iterables
 
- Son aquellos objetos que pueden ser iterados o indexados, como listas, tuplas, cadenas y diccionarios.

## Iteradores

Son objetos que hacen referencia a un elemento y tienen un método next que permite hacer referencia al siguiente.

- Para verificar si un objeto es iterable, se puede usar isinstance().

Ejemplo con isinstance()

```python 
from collections.abc import Iterable

lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10

print(isinstance(lista, Iterable))  # True
print(isinstance(cadena, Iterable)) # True
print(isinstance(numero, Iterable)) # False
```

## Ejemplo con iter() y next()
```python
lista = [5, 6, 3, 2]
it = iter(lista)

print(next(it)) # 5
print(next(it)) # 6
print(next(it)) # 3
```

## For Anidados
- Es posible anidar bucles for para iterar sobre estructuras de datos más complejas, como listas de listas.

Ejemplo con Lista de Listas

```python
lista = [[56, 34, 1], [12, 4, 5], [9, 4, 3]]

for i in lista:
    print(i)

# Salida:
# [56, 34, 1]
# [12, 4, 5]
# [9, 4, 3]

for i in lista:
    for j in i:
        print(j)

# Salida: 56, 34, 1, 12, 4, 5, 9, 4, 3
```
## Iterar Cadena al Revés
Haciendo uso de [::-1] se puede iterar la lista desde el último al primer elemento.

```python
texto = "Python"
for i in texto[::-1]:
    print(i) # n, o, h, t, y, P
```

## Iterar Saltándose Elementos
Con [::2] vamos tomando un elemento sí y otro no.

```python
texto = "Python"
for i en texto[::2]:
    print(i) # P, t, o
```
## Uso con List Comprehensions
```python
print(sum(i for i in range(10)))

# Salida: 45
```
## Conclusión
El bucle for en Python es una herramienta poderosa y versátil, permitiendo iterar sobre una amplia variedad de estructuras de datos de manera eficiente y concisa.


# Ejercicios

- [Ejemplos](./ejercicios/README.md)