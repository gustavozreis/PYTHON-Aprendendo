# Combinations, Permutations e Product -- Itertools

from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino'],
]

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()
    
print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))