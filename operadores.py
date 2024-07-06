#OPERADORES ARITMÉTICOS
#SUMA
print( 5 + 5)
#RESTA
print( 5 - 2)
#MULTIPLICACIÓN
print( 5 * 5)
#DIVISIÓN
print(type(10/2))
#DIVISIÓN ENTERA
print(type(11//2))
#POTENCIA
print( 2 **3)
#MÓDULO
print(40 % 8)
print(41 % 8)
print(42 %  8)
print(14 % 2)
print(21 % 2)

#PARANTESIS SE UTILIZA PARA EL ORDEN DE LAS OPERACIONES

a = 2 
operacion = (a + 2) ** 3
print(operacion)

a = 4 ; b = 3;
operacion = (a + 5) / (b - 1)
print(operacion)

#OPERADORES RELACIONALES
#IGUAL QUE
print(5 == 5)
print(5 == 2)
# #DISTINTO QUE
print(5 != 5)
print( 2 != 3)
# #MAYOR QUE
print(4 > 2)
print( 4 > 6)
# #MENOR QUE
print( 3 < 2)
print( 3 < 4)
# #MAYOR O IGUAL QUE
print( 4 >= 4)
print( 4>= 3)
# #MENOR O IGUAL QUE
print( 5 <=5)
print( 5 <= 3)

#CONECTORES LÓGICOS
#AND CONJUNCIÓN
# 0 0 = 0
# 0 1 = 0
# 1 0 = 0
# 1 1 = 1
print(4== 3 and 3 < 2)
print(4== 3 and 3 == 3)
print(4== 4 and 3 != 3)
print(4== 4 and 3 == 3)
#OR DISYUNCION
#0 0 = 0
#0 1 = 1
#1 0 = 1
#1 1 = 1
print(4== 3 or 3 < 2)
print(4== 3 or 3 == 3)
print(4== 4 or 3 != 3)
print(4== 4 or 3 == 3)
#NOT NEGACIÓN
print(not 3!=3)

#OPERADORES DE INCREMENTO Y DECREMENTO
# +=
a = 0
# a = a +5
a+=5
a+= 5
print(a)
# -=
b = 10
# b= b - 5
b -= 5
print(b)
# *=
c = 2
# c = c * 2
c *=2
c *= 2
print(c)
# /=
d = 20
# d = d / 2
d /=2
print(d)