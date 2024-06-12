# Inversión de una Cadena: Escribe un programa que invierta una cadena de caracteres dada por el usuario.

palabra_usuario = input('ingresa una palabra')
palabra_invertida = ''

for l in palabra_usuario:
    palabra_invertida = l + palabra_invertida

print(palabra_invertida)
