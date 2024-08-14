nome = input ("Escreva seu nome: ")
idade = input ("Escreva sua idade: ")
nome_invertido = nome[::-1]

if nome != "" and idade != "": 
    print("Seu nome e", nome)
    print("Seu nome invertido e", nome_invertido)



    if ' ' in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome nao contem espaço")
    
    print(f'Seu nome tem {len(nome)}letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
    
else:
    print("Desculpe, voce deixou campos vazio =(")
    
