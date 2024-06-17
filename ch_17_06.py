# DIA 5
# Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.

claves = ['apellido','profesion','edad']
valores = ['pedersen','sonidista','28']

def dict_maker(key,value):
    diccionario = {}
    for k, v in zip(key, value):
        diccionario[k] = v
    return diccionario

print(dict_maker(claves,valores))