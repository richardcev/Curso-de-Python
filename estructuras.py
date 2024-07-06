#ESTRUCTURAS CONDICIONALES
#IF CONDICION_1:
    #INSTRUCCION_1
    #INSTRUCCION_2
    #INSTRUCCION_3
#ELSE:
    #INSTRUCCION_A


semaforo = "rojo"
if semaforo == "verde":
    print("Cruzar")
else:
    print("Parar")

# Si la compra es mayor que $100, aplicar un descuento del 10%
compra = 50
if compra > 100:
    total = compra * 0.90
    print(total)

# Escribir un programa en python que imprima  “es par” si el
# número ingresado es par y “es impar” si el número ingresado es impar
numero = int(input("Ingrese un número: "))
if numero % 2 ==0:
    print("es par")
else:
    print("es impar")


#ELIF
#ingrese una edad, niño, adolescente, adulto, adulto mayor
edad = int(input("Ingrese una edad: "))
if edad < 0:
    print("Edad inválida")
elif edad < 13:
    print("Eres un niño")
elif edad < 20:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
