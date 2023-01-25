# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

cities_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_list = ['BA', 'SP', 'MG', 'RJ']


def zipper(list1, list2):
    min_range = min(len(list1), len(list2))
    return [
        (list1[i], list2[i]) for i in range(min_range)
    ]
        
print(zipper(cities_list, states_list))
print(list(zip(cities_list, states_list)))
print(list(zip_longest(states_list, cities_list, fillvalue='VAZIO')))