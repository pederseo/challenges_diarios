# DIA 5
# Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

def celsius_a_Fahrenheit(celsius):
    fahrenheit = celsius - 32 * 5/9
    print(f'{int(celsius)} celsius = {int(fahrenheit)} fahrenheit')

def fahrenheit_a_celsius(fahrenheit):
    celsius = fahrenheit * 9/5 + 32
    print(f'{int(fahrenheit)} fahrenheit = {int(celsius)} celsius')

c = celsius_a_Fahrenheit(45)
f = fahrenheit_a_celsius(113)

