lista = [1, 2, 3, 4]
print(lista)
lista2 = [11.22, 12.45, 45.25, 55.26]
lista3= ["David", "Adrian", "Jose", "Jorge"]
lista4 = [False, True, False, False]
lista5 = [1, "David", False, 22.25]
lista6 = [[1,2,3] , [4,5,6]]
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista6)

#OPERACIONES
paises = ["Ecuador", "Chile", "Venezuela", "Argentina"]
pais = paises[-1]
print(pais)
print(paises[0:3])

#CONCATENACION
lista= [1,2,3,4]
lista2 = [5,6,7,8]
lista3 = lista + lista2
print(lista3)

letras = ["X"] *8
print(letras)

#IN
lista= [1,2,3,4]
if 48 in lista:
    print("se encuentra")

#DELETE
del lista[2]
print(lista)

#LEN
lista = [1,2,-2.5,40,5,5.2,7,8]
print(len(lista))
print(max(lista))
print(min(lista))

lista = ["abc", "david", "uva", "zcf"]
print(max(lista))
print(min(lista))

#index
print(lista.index("uva"))
#count
lista = [1,2,3,4,2,3,5,6,2,5]
print(lista.count(65))

#append
lista= [1,2,3,4]
lista.append(5)
lista.append(56)
lista.append(47)

print(lista)

#extend
lista= [1,2,3,4]
lista2 = [5,6,7]
lista.extend(lista2)
print(lista)

#CAMBIAR LOS ELEMENTOS
lista= ["david", "luis", "jose"]
print(lista)
lista[1] = "jorge"
print(lista)

# Lista de meses
# Lista de días de cada mes
# Mostrar cuantos días tiene un mes ingresado por consola
# Cambiar el número de días de Febrero

meses = ["Enero", "Febrero", "Marzo" , "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dias[1] = 29

mes = input("Ingrese un mes: ")
indice = meses.index(mes)
dia = dias[indice]
print(f"{mes} tiene {dia} días")