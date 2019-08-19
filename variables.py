#variables
nombre = "Hola Froy"
print(nombre)

x,libro = 100,"Lord of the Rings"
print(x,libro)

#constante
PI = 3.1416

#dir permite conocer los métodos que puedo utilizar conuna variable
print(dir(PI))

print(nombre.upper())
print(nombre.lower())
print(nombre.replace('Froy','Eve').upper)
print(nombre.count('r')) #cuenta cuantas letras r hay
nombre.find('a') #devuelve la posición donde se encuentra la letra
len(nombre)