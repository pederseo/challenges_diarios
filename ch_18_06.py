# DIA 5
# Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

def celsius_a_Fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    print(f'{int(celsius)} celsius = {int(fahrenheit)} fahrenheit')

celsius_a_Fahrenheit(45)


