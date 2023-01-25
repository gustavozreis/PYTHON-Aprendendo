"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 3, 4, 5, 7, 8, 3, 8, 8, 1],
]

def check_duplicate(int_list):
    result = -1
    int_set = set()
    
    for int_digit in int_list:
        if int_digit in int_set:
            result = int_digit
            break
        
        int_set.add(int_digit)
    
    return result
    
       
for int_list in lista_de_listas_de_inteiros:
    print(int_list, check_duplicate(int_list))
    print()

# for lista in lista_de_listas_de_inteiros:
#     s1 = set(lista)
#     duplicated_numbers_with_index = []
    
#     if len(s1) == len(lista):
#         print(f'O resultado é {-1}')
#         print()
#     else:
#         for number_index, number_to_check in enumerate(lista):
#             # checa se tem duplicado do number_to_check
#             if lista.count(number_to_check) > 1:
#                 # checa se já existe um dict com a key igual ao number_to_check
#                 contains_this_key = False
#                 for item in duplicated_numbers_with_index:
#                     if item['number'] == number_to_check:
#                         contains_this_key = True
#                         break
                
#                 if contains_this_key == False:
#                     duplicated_numbers_with_index.append({'number':number_to_check, 'indexes':[number_index]})
#                 else:
#                     # adiciona o índice que o número aparece na sua lista de índices
#                     for i, item in enumerate(duplicated_numbers_with_index):
#                         if item['number'] == number_to_check:
#                             item['indexes'].append(number_index)
        
#         result_list = []                
#         for item in duplicated_numbers_with_index:
#             if len(result_list) == 0:
#                 result_list = [item['number'], item['indexes'][1]] 
#             if item['indexes'][1] < result_list[1]:
#                 result_list = [item['number'], item['indexes'][1]] 
        
#         print(f'O resultado é {result_list[0]}')
#         print()   