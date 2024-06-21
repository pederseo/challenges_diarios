# DIA 7
# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import random

longitud = random.randint(8,16)

numeros = '1234567890'

abecedario_minusculas = 'abcdefghijklmnopqrstuvwxyz'

abecedario_mayusculas = abecedario_minusculas.upper()

list(numeros)
list(abecedario_minusculas)
list(abecedario_mayusculas)
caracteres_especiales = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

lista = [numeros,abecedario_mayusculas,abecedario_minusculas,caracteres_especiales]

contrasena = ''
for i in range(longitud):
    seleccion = random.choice(lista)

    caracteres = random.choice(seleccion)

    contrasena = contrasena + caracteres

print(contrasena)