frase = 'O Python e uma linguagem de programaçao '\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum.'

i = 0

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_a_letra_apareceu = frase.count(letra_atual)


    print(letra_atual)
    i += 1


    