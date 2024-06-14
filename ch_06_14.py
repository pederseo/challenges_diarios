# DIA 4
# Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

cantidad_numeros = input('cuantos numeros desea ingresar? ')
lista_numeros = []
cont = int(cantidad_numeros)

for num in range(int(cantidad_numeros)):
    lista_numeros.append(input(f'ingresa un numero "cantidad faltante ({cont})" '))
    cont = cont - 1

lista_ascendente = sorted(lista_numeros)
print(f'\nesta es tu lista de numeros: {lista_numeros}\ny esta es tu lista de numeros de forma ordenada: {lista_ascendente}')
