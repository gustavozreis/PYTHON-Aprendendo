# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply(*args):
    result = 1
    for digit in args:
        result *= digit
    return result

print(multiply(10, 10, 10))