# DIA 6
# Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

import random

jugador1 = input('elije: piedra papel o tijera: ')
jugador2 = ['piedra','papel','tijera']
opciones = random.choice(jugador2)

if 'piedra' in jugador1:
    if 'papel' in opciones:
        print(f'jugador2 elijio {opciones}: PERDISTE')
    if 'tijera' in opciones:
        print('GANASTE')

if 'papel' in jugador1:
    if 'tijera' in opciones:
        print(f'jugador2 elijio {opciones}: PERDISTE')
    if 'piedra' in opciones:
        print('GANASTE')
        
if 'tijera' in jugador1:
    if 'piedra' in opciones:
        print(f'jugador2 elijio {opciones}: PERDISTE')
    if 'papel' in opciones:
        print('GANASTE')

if jugador1 == opciones:
    print(f'jugador2 elijio {opciones}: EMPATE')

