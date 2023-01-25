# Exercício - sistema de perguntas e respostas

import enum


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

user_points = 0

for pergunta in perguntas:
    
    print(pergunta['Pergunta'])
    
    for i, option in enumerate(pergunta['Opções']):
        print(f'{i}) {option}')
    
    correct_answer = 0        
    for answer in pergunta['Opções']:
        if answer == pergunta['Resposta']:
            break
        else:
            correct_answer += 1       
        
    user_answer = input('Escolha uma opção: ')
    if(user_answer) == str(correct_answer):
        user_points += 1
        print('Você acertou!\n')
    else:
        print('Resposta errada.\n')
        
print(f'Você acertou {user_points} perguntas!')