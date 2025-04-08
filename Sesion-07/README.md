# Ejemplos Básicos de Python: Funciones y Listas

Este documento presenta ejemplos básicos de cómo utilizar **funciones** y **listas** en Python.

## 📌 Función que suma dos números
```python
def suma(a, b):
    return a + b
```

- resultado = suma(5, 3)
- print("La suma es:", resultado)  # Salida: La suma es: 8

# Ejemplo 02

```python
def encontrar_maximo(lista):
    return max(lista)

numeros = [10, 5, 20, 8]
print("El número más grande es:", encontrar_maximo(numeros))  # Salida: El número más grande es: 20
```
# Ejemplo 03
```python
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

colores = ["rojo", "verde", "azul"]
imprimir_lista(colores)

```

# Ejemplo 04

```python
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

frutas = ["manzana", "plátano"]
nueva_lista = agregar_elemento(frutas, "uva")
print(nueva_lista)  # Salida: ['manzana', 'plátano', 'uva']

```

# Ejemplo 05

```python
def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [4, 7, 2, 9]
print("La suma de la lista es:", suma_lista(numeros))  # Salida: La suma de la lista es: 22
```

# Ejemplo 06
```python
def contar_ocurrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

frutas = ["manzana", "pera", "manzana", "uva", "manzana"]
print("La cantidad de 'manzana' es:", contar_ocurrencias(frutas, "manzana"))  # Salida: La cantidad de 'manzana' es: 3
```

# Ejemplo 07
```python
def cuadrados(lista):
    cuadrados_lista = []
    for numero in lista:
        cuadrados_lista.append(numero ** 2)
    return cuadrados_lista

numeros = [1, 2, 3, 4]
print("Lista de cuadrados:", cuadrados(numeros))  # Salida: Lista de cuadrados: [1, 4, 9, 16]
```

# Ejemplo 08

```python
def filtrar_mayores(lista, limite):
    mayores = []
    for numero in lista:
        if numero > limite:
            mayores.append(numero)
    return mayores

numeros = [10, 20, 5, 30, 15]
print("Números mayores a 15:", filtrar_mayores(numeros, 15))  # Salida: Números mayores a 15: [20, 30]
```