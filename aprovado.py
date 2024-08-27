nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2
print(f'Sua media foi: {media}')

if media >= 7:
    print('Voce foi aprovado')
elif media < 4:
    print('Voce foi reprovado')
elif media >= 4 and media < 7:
    print('Voce precisa fazer a prova final')

else:
    print('Digite sua nota')
