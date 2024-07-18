#()
tupla = ("a", "b", "c", "d", 4)
# tupla = (1,)
print(tupla)

#INDICES
print(tupla[1:3])

tupla = ("a", "b", "c", "d", 4)
#INMUTABLES
# tupla[0] = "H"
# print(tupla)

for i in tupla:
    print(i)

#CONVERSIONES DE LISTAS A TUPLAS Y VICEVERSA
lista = [1,2,3,4,5]
print(lista)
tupla = tuple(lista)
print(tupla)
conversion = list(tupla)
print(conversion)

#OPERADORES
numeros1= (1,2,3)
numeros2= (4,5,6)
total = numeros1 + numeros2
print(total)

numeros = (1,2) * 3
print(numeros)

if 7 in numeros:
    print("se encuentra")
else:
    print("no se encuentra")


#FUNCIONES
numeros = (1,2,3,4,5,6)
print(len(numeros))

print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(numeros)
del(numeros)
print(numeros)