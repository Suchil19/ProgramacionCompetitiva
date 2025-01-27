#01-Hola Mundo
print("Hola Mundo")

#02-Creación de variables
a = 10
b = 20
suma = a + b
print(suma)

#03-Ejemplo de concatenación
a = 10
b = 20
suma = a + b
print("este es tu resultadi", suma)

#04-Declara tus variables con un input
nombre = str(input("Cúal es tu nombre "))
saludo = (" bienvenido a un nuevo curso ")
print("Hola " + nombre + saludo )

#05-Tipos de datos - int
a = int(input("escribe tu primer valor"))
b = int(input("escribe tu segundo valor"))
suma = a + b
print("el resultado es ... ", suma)

#06-Float
nombre = str(input("Cual es tu nombre"))
peso = float(input("Cual es tu peso"))
# Concatenar el string y el float
print("Gracias" + nombre + "tu peso es de ", peso, "kg")

#07-Tipos de datos - float
a = float(input("escribe tu primer valor"))
b = float(input("escribe tu segundo valor"))
div = a / b
print("el resultado es ... ", div)

#08-Calculadora
nombre = str(input("¿Cual es tu nombre?"))
print("hola " +  nombre + " vamos a varias operaciones")
num_uno = float(input("por favor escribe el primer valor"))
num_dos = float(input("por favor escribe el segundo valor"))
resultado1 = num_uno + num_dos
resultado2 = num_uno / num_dos
resultado3 = num_uno * num_dos
print(nombre + " el resultado de la suma es:", resultado1)
print(nombre + " el resultado de la division es:", resultado2)
print(nombre + " el resultado de la multiplicacion es:", resultado3)


#10- Traductor
print( " **** selecciona una opcion **** ")
print(nombre + " presiona 1 para traductor de colores: inglés a español")
print(nombre + " presiona 2 para traductor de colores:  español a inglés")
print(nombre + " presiona 3 para traductor de colores:  español a frances")
print("**********")
opcion = int(input("Escribe la opción que deseas usar "))
#Opción 1 Español a ingles
if opcion == 1:
  print("Elegiste inglés a español")
  opcion_uno = input("escribe la palabra que deseas traducir")
  if opcion_uno == "blue":
    print("la palabra significa AZUL") 
  elif opcion_uno == "red":
    print("la palabra es ROJO") 
  else:
    print("no se conoce el color")
    
# Opción 2 Ingles a español
elif opcion == 2:
  print("traductor de español a ingles")
  opcion_dos = input("que palabra deseas traducir")
  if opcion_dos == "rojo":
    print("the color is red")
  elif opcion_dos == "azul":
    print("the color is blue")
  else:
    print("opción no valida")
#Opcion 3 Español a Frances
elif opcion == 3:
  print("traductor español a frances que color quieres traducir?")
#Opcion no valida en el menu de opciones
else:
  print("opción no válida")