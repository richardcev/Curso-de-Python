#F STRING
nombre = "Richard"
apellido = "Cevallos"
edad = 25
pi = 3.14159
print(f"Hola me llamo {nombre} {apellido} y tengo {edad} años")
print(f"El valor de pi es {pi:.2f}")

# format()
print("Hola me llamo {1} {0} y tengo {2} años".format(nombre, apellido, edad))
print("El valor de pi es {:.2f}".format(pi))


print("Carlos toca {instrumento1} y {instrumento2}".format(instrumento1= "piano", instrumento2= "bateria"))

#SIGNO DE %
print("Hola me llamo %s %s tengo %d años" % (nombre, apellido, edad))
print("El valor de pi es %.2f" % pi)

print("Hola \" ")
print("Hola \\")
print("Hola me llamo Richard Cevallos \n y tengo 25 años")
print("Hola me llamo Richard Cevallos \t y tengo 25 años")