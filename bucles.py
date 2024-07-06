#WHILE
#WHILE CONDICION:
    #INSTRUCCION1
    #INSTRUCCION2
    #INSTRUCCION3
    #ACTUALIZAR CONDICION

# Escribir un programa que permita el ingreso de 5 números
i =0
while i < 5:
    numero = int(input("Ingrese un número: "))
    i += 1
print("Se ha terminado el programa")

# Escribir un programa que permita el usuario el ingreso de n números
repeticiones = int(input("Cuantos números deseas ingresar ? "))
repeticion= 0
while repeticion < repeticiones:
    numero = int(input("Ingrese un número: "))
    repeticion +=1

numero = 0
while numero < 10:
    print(numero)
    numero += 1

print("Fin del programa")

#FOR
#SECUENCIAS DE NÚMEROS
#LISTAS
#CADENAS DE CARACTERES

# print(list(range(9)))
#FOR ITEM IN ESTRUCTURA:
    #INSTRUCCION1
    #INSTRUCCION2

for item in range(5):
    print(item)

lista = ["Ecuador", "Argentina", "Chile", "Paraguay"]
for pais in lista:
    print(pais)

cadena = "Ecuador"
for letra in cadena:
    print(letra)

# Escribir un programa que cuente el número de letras en una palabra.
numero_letras = 0
palabra = "Etiopía"
for letra in palabra:
    numero_letras+=1
print(f"La palabra tiene {numero_letras} letras")


# Escribir un programa que permite el ingreso de n números.
n = int(input("Cuantos numeros desea ingresar? "))
for i in range(n):
    numero = int(input("Ingrese un número: "))

print("Fin del programa")