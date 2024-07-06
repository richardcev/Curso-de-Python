import random

numero = random.random()
print(numero)

numero = random.randint(1,10)
print(numero)

numero = random.randrange(5)
print(numero)

numero = random.uniform(1.5 , 4.5)
print(numero)

frutas = ["Banana", "manzana", "pera" , "uva"]
print(random.choice(frutas))
print(random.sample(frutas, 2))
random.shuffle(frutas)
print(frutas)

letras= 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'
especiales= '$#%@-'

caracteres = letras + numeros + especiales
longitud = 10

contraseña_lista = random.sample(caracteres, longitud)
# print(contraseña_lista)
contraseña = ''.join(contraseña_lista)
print(contraseña)