"""
Formatacao basica de strings
s- String
d -int
f -float
.<numero de digitos>f
(carctere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
nome = 'Gustavo'
preco = 100.987689
variavel = '%s, o preço e R$%f'%(nome,preco)
print(variavel)