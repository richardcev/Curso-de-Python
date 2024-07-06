#CONCATENACIÓN
print("Hola" + " mundo")
nombre = "Richard"
apellido = " Cevallos"
edad = 25
print("Hola me llamo " + nombre + apellido + " y tengo " + str(edad) + " años")

print(3 * "programas ")

#INDICES
fruta = "banana"
print(fruta[2])

saludo = "HELLO"

longitud = len(saludo)
print(saludo[longitud - 1])
print(longitud)

#SLICING
s = "Fundamentos"
print(s[1:4])
print(s[:5])
print(s[5:])
print(s[:])
print(s[-2:])
print(s[1:7:2])
print(s[::-1])

url = "www.espol.edu.ec"
url1 = "www.uchile.edu.cl"
url2 = "www.unam.edu.mx"

print(url[-2:])
print(url1[-2:])
print(url2[-2:])

#BÚSQUEDAS
cadena = "hola"
if "u" in cadena:
    print("se encuentra")

print(cadena.index("a"))
print(cadena.find("oa"))

#FUNCIONES DE FORMATO
cadena = "bienvenido a mi aplicación"
print(cadena.capitalize())
cadena = "hola mundo"
print(cadena.lower())
print(cadena.upper())
print(cadena.swapcase())
print(cadena.title())

#OTRAS FUNCIONES
print(cadena.count("o"))
print(cadena.endswith("do"))
print(cadena.startswith("fg"))

cadena = "hola me llamo David"
print(cadena.isalnum())
print(cadena.isalpha())
print(cadena.isdigit())
print(cadena.isdecimal())
print(cadena.isupper())
print(cadena.islower())

print(cadena.split(" "))
cadena = "   hola  mundo  "
cadena = "----hola  mundo----"
print(cadena.strip("-"))
print(cadena.replace("mundo", "David"))

cadena = "hola"
# cadena[0] = "k"
cadena = "hola mundo"
print(cadena)