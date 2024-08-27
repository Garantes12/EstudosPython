while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite um numero: ')
    operador = input('Digite o operador (+-*/): ')

    numero_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos dos numeros digitados sao invalidos')
        continue

    operadore_permitidos = '+-/*'

    if operador not in operadore_permitidos:
        print('Operador Invalido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta confira o resultado abaixo')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/': 
        print(num_1_float / num_2_float)
    elif operador == '*': 
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Digite [s]air para sair: ').lower().startswith('s')
    
    if sair:
        print('Saindo')
        break