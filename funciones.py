#DIVIDE Y VENCERÁS

#TRASNFERENCIA Y RETORNO

#def nombre_de_la_funcion(parametros):
    #instruccion1
    #instruccion2
    #instruccion3



def sumar_numeros(a ,b= 0):
    suma = a + b
    print(suma)

# numero = sumar_numeros(2, 10)
sumar_numeros(2, 10)

def printinfo(nombre, edad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")

printinfo(edad = 18 , nombre = "Richard")

#PASOS DE PARÁMETROS POR VALOR Y REFERENCIA
#POR VALOR: tipos de datos primitivos

x = 5
def fun(x):
    x = x **2
    y = 2*x + 1
    return y

y = fun(x)
print(y)
print(x)

#POR REFERENCIA: listas, tuplas
lista = [1,2,3,4]
def cambio(lista):
    lista[0] = "a"
    return lista

nuevalista = cambio(lista)
print(nuevalista)
print(lista)

def mayor(a,b):
    if a> b:
        return a, b
    else:
        return b, a
a , b = mayor(20,10)
print(a,b)

def inalcanzable():
    return "alcanzable"
    mensaje = "inalcanzble"
    return mensaje
print(inalcanzable())


variable = 12
def alcance():
    global variable
    variable = "hola"
    return variable

alcance()
print(variable)

