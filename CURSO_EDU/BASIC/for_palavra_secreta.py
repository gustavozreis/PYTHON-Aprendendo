from operator import contains
import random

secret_words = ['perfume', 'cachorro', 'documento', 'mouse', 'celular', 'computador', 'cabeça', 'guarana', 'picanha']

secret_word_chosen = secret_words[random.randint(0, len(secret_words) - 1)]

secret_word_hidden = '*' * len(secret_word_chosen)

max_rounds_allowed = 10

number_of_guesses = 0

index = 0

print('Adivinhe a palavra!\nVocê tem 10 tentativas!')

for round in range(0,max_rounds_allowed):
    
    if '*' in secret_word_hidden:
    
        number_of_guesses += 1
        print(f'\nTentativa número {number_of_guesses}')
        
        letter_guessed = input('Digite uma letra: ')
        if len(letter_guessed) > 1:
            print('Digite apenas uma letra.')    
        else:
            for char in secret_word_chosen:
                if char == letter_guessed:
                    secret_word_hidden = secret_word_hidden[:index] + letter_guessed + secret_word_hidden[index+1:]
                    index += 1 
                else:
                    index += 1
            
            index = 0        
            print(secret_word_hidden)        

    else:
        print(f'Parabéns, você acertou a palavra {secret_word_hidden}!')
        break
    
print('\nVocê não tem mais tentativas e perdeu o jogo.\n')


            
        
        
