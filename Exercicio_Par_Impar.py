"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input("Digite um numero: ")

try:
    entrada_int =  int(entrada) 
    par_impar = entrada_int % 2 == 0
    par_impar_text = "impar"

    if par_impar:
        par_impar_text = "par"
    print(f'O numero {entrada_int} e {par_impar_text}')
except:
    print('Voce nao digitou um numero inteiro')    
