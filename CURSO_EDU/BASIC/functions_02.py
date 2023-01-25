# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def create_multiplication(mult):
    def multiply(num):
        return num * mult
    return multiply

duplicate = create_multiplication(2)
triplicate = create_multiplication(3)
quadruplicate = create_multiplication(4)

num_input = int(input('Insira um número: \n'))

print(f'O dobro é {duplicate(num_input)}, o triplo é {triplicate(num_input)}, o quadruplo é {quadruplicate(num_input)}')