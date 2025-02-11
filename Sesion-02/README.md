# Concatenación, Entradas de Datos y Tipos de Datos

## Instalación Visual Studio
- Antes de comenzar a codificar tendremos que instalar nuestro entorno de desarrollo, no te preocupes te guiaremos paso a paso 😉.

# Instalación

- Instala Visual Studio paso a paso en - [este turorial](/Manuales/InstalacionVisualStudio/README.md)
![Visual Studio](/Manuales/InstalacionVisualStudio/img/visual.png) 

## Concatenación en Python

## ¿Qué es la Concatenación?

La concatenación en Python es el proceso de unir dos o más cadenas de texto (strings) para formar una sola cadena. Es una operación común en la manipulación de texto y se puede realizar de varias maneras en Python.

## Métodos de Concatenación

### Usando el Operador `+`

El operador `+` es el método más simple y directo para concatenar cadenas en Python.

```python
cadena1 = "Hola"
cadena2 = "Mundo"
resultado = cadena1 + " " + cadena2
# Salida: Hola Mundo
print(resultado) 

```

## Entrada de Datos en Python

### ¿Qué es la Entrada de Datos?

La entrada de datos en Python permite a los usuarios proporcionar información al programa mientras se está ejecutando. Esta información se puede utilizar para personalizar la ejecución del programa, realizar cálculos, tomar decisiones y mucho más. La función principal para recibir entrada de datos del usuario en Python es `input()`.

### Uso de la Función `input()`

La función `input()` se utiliza para capturar la entrada del usuario desde la consola. Cuando se llama a esta función, el programa se detiene y espera a que el usuario ingrese un texto y presione Enter. El texto ingresado se devuelve como una cadena (string).

### Ejemplo Básico input

```python
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre + "!")

```