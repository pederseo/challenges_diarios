
#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

palabra = "challenge dia 3"
vocales = "aeiou"
cont_vocales = ""

for p in palabra:
    for v in vocales:
        if v in p:
            cont_vocales = cont_vocales+p
print(f"la cantidad de vocales dentro de la frase: '{palabra}' es ({len(cont_vocales)})")
