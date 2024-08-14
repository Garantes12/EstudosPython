primeiro_valor= input  ('Digite um valor: ')
segundo_valor= input  ('Digite outro valor: ')

#if primeiro_valor > segundo_valor :
 #   print(primeiro_valor, 'e maior do que segundo_valor')
#elif segundo_valor > primeiro_valor:
 #   print(segundo_valor, 'e maior que o primeiro_valor')

# solucao correta do exercicio
if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} e maior ou igual' f'ao{segundo_valor=}')
else:
    print(f'{segundo_valor=} e maior', f'do que {primeiro_valor=}')