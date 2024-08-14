nome = 'Gustavo Correia'
altura = 1.83
peso = 70

# calculo IMC = peso / (altura x altura)
imc = peso / (altura * altura)

# f-strings
linha1 = f'{nome} tem {altura:.2f} de altura'
linha2= f'pesa {peso} quilos e seu imc e {imc}'

#print(nome, 'tem', altura, 'de altura', 'pesa', peso, 'quilos', 'e seu IMC e', imc)
print(linha1)
print(linha2)