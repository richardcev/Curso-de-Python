# Programa que cuente el número de “a” en un palabra
palabra = input("Ingrese una palabra: ")
numero_letras= 0
for letra in palabra:
    print(letra)
    if letra == "a":
        print("TERMINADO")
        numero_letras += 1
        continue
        print("ESTO NO SE IMPRIME")
    
print(f"{palabra} tiene {numero_letras} letras a")

# Programa que muestre las tablas de multiplicar del 1 al 10.
for i in range(1,11):
    print(f"TABLA DEL {i}")
    for j in range(1,11):
        total = i * j
        print(f"{i} X {j} = {total}")


i = 1
while i < 11:
    j = 1
    while j < 11:
        total = i*j
        print(f"{i} X {j} = {total}")
        j +=1
    i +=1


#EL USUARIO DEBE INGRESAR 3 LADOS, PARA DETERMINAR SI 
#UN TRIÁNGULO ES EQUILÁTERO, ISÓSCELES O ESCALENO

lado1 = input("Ingrese lado1: ")

lados =[]
for i in range(1,4):
    lado = input(f"Ingrese lado{i}: ")
    lados.append(lado)

a, b , c= lados
print(a,b,c)

if a == b and b ==c:
    print("El triángulo es equilatero")
else:
    if a == b or b ==c or a == c:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")



#el programa debe mostrar el color obtenido al mezclar dos colores en la pantalla

print("Este programa mezcla dos colores")
color1 = input("Elija el primer color, Azul(a)  o  Rojo(r): ")
if color1 == "a":
    color2 = input("Elija el segundo color, Verde(v)  o  Amarillo(a): ")
    if color2 =="v":
        print("La mezcla entre azul y verde es púrpura")
    else:
        print("La mezcla entre azul y amarillo es verde")
else:
    color2 = input("Elija el segundo color, Blanco(b)  o  Amarillo(a): ")
    if color2 =="b":
        print("La mezcla entre rojo y blanco es rosa")
    else:
        print("La mezcla entre rojo y amarillo es naranja")


