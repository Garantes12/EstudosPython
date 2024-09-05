"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z):
    print(f'{x =} y= {y} {z=}', '|','x + y = ', x + y + z )

soma(x=1, z=2, y=5)

print(1, 5, 9, sep='.')