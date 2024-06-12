# DIA 2
# Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

numero_usuario = 5
contador = 1
print(f'tabla de multiplicar del {numero_usuario}')
while contador <= 10:
    resultado = numero_usuario * contador
    print(f'{numero_usuario} * {contador} = {resultado}')
    contador = contador + 1
