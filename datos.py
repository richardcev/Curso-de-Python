# #STRINGS O CADENAS
# print(type('Hola mundo me llamo David Cevallos'))
# print(type("55"))
# #NÚMEROS
# #ENTEROS O INT
# print(type(5))
# print(type(0))
# print(type(-6))
# #DECIMALES O FLOAT
# print(type(4.6))
# print(type(-5.9))
# #LÓGICOS O BOOLEANOS
# print(type(True))
# print(type(False))
# print( 9 > 5)
# print( 4 < 2)


# #EL ESTADO CIVIL DE UNA PERSONA - STRING
# print("SOLTERO")
# #LA CANTIDAD DE HIJOS DE UNA PAREJA - INT
# print(3)
# # ¿ EL ESTUDIANTE TIENE BECA ? - booleano
# print(True)
# # EL PRECIO DE UN PRODUCTO EN UNA TIENDA ONLINE - FLOAT
# print(99.99)
# #EL COLOR DE UN VESTIDO -STRING
# print("AMARILLO") 
# #TU NÚMERO DE CÉDULA -STRING
# print("0931492045")
# #TU NÚMERO DE TELÉFONO -STRING
# print("0980185987")


x = 5
y= 6
print(x)
print(y)
x = 8
y= 10
print(x)
print(y)

dia = "Lunes"
pi = 3.14
tiene_beca = True
precio_producto = 99.99

#ASIGNACIÓN EN LA MISMA LINEA
a = 1 ; b = 2 ; c =3
print(a, b , c)
#ASIGNACIÓN MÚLTIPLE
dia, mes, anio = "Martes", "Mayo", "2024"
print(dia, mes, anio)
#ASIGNACIÓN DEL MISMO VALOR
x = y = 46
print(x, y)
#ASIGNACIÓN DE INTERMCABIO
base, altura = 12 , 24
base , altura = altura, base
print(base, altura)

cedula = "0931492045"
fecha_actual = "11-12-2024"
fechaActual = "11-12-2024"
# fecha-actual = "11-12-2024"
# 1numero = 5
# numero1= 5
# DIA = "Lunes"
# $fechaActual = 2

# and = 5
# class = 6

# and  assert  break  class  continue def  del
# elif  else  except  exec finally  for  from  global  if  import in  input  
# is  lambda  next  not  or  pass  print  raise  return  try  while yield 


#CALCULE EL TOTAL DE UNA COMPRA DE DOS PRODUCTOS INCLUYENDO IVA, EL PRIMER PRODUCTO CUESTA $45.25 Y EL SEGUNDO $22.23
precio_producto1 = 45.25
precio_producto2 = 22.23
iva= 0.12
subtotal = precio_producto1 + precio_producto2
total = subtotal * (1 + iva)
print(f"{total:.2f}")
