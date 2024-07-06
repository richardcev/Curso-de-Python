#int()
#float()
#str()
#bool()

print(int(3.14))
print(int(3.9999))
print(int(-3.9999))
print(int(14))
print(type(int("55")))
print(int("2345"))

print(float(14))
print(type(float("14.566")))

print(type(str(45)))
print(str(4.568))

print(bool(1))
print(bool(0))
print(int(True))
print(int(False))

nombre = input("Ingrese un nombre: ")
print(nombre)

numero = input("Ingrese un número: ")
print(type(int(numero)))

#Ingreso de base y altura
base = input("Ingrese la base: ")
altura= input("Ingrese la altura: ")
print("La base es", base, "y la altura es", altura)

#AREA DE UN CIRCULO: PI * RADIO **2
respuesta = input("¿Cual es su radio? ")
radio = float(respuesta)
area = 3.14159 * radio **2
print("El área del círculo es", f"{area:.2f}")
