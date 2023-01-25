from re import M


meu_nome = 'Gustavo Zanardi dos Reis'

mn_index = 0

while mn_index <= len(meu_nome):
    if meu_nome[mn_index].isalpha() == True:
        print(f'Letra: {meu_nome[mn_index]}')
        mn_index += 1
    else:
        print('ESPAÇO')
        mn_index += 1    
    