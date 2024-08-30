import os

lista =[]

while True:
    print('Selecione uma opçao: ')
    opcao = input ('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        print('i')
    elif opcao == 'a':
        indice_str = input(
            'Escolha o indice para apagar:'
        )
        try:    
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite numero int')
        except IndexError:
            print('Nao existe na lista')
    elif opcao == ('l'):
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por Favor, escolha i,a ou l')

        

