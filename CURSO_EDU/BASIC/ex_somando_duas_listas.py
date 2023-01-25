"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

def sum_lists(list1, list2):
    max_range = min(len(list1), len(list2))
    return [
        list1[i] + list2[i]
        for i in range(max_range)
    ]
    
def sum_lists_zip(list1, list2):
    return [
        x + y
        for x, y in zip(list1, list2)
    ]
    
print(list(zip(lista_a, lista_b)))
print(sum_lists_zip(lista_a, lista_b))