# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

lista = [12, 35, 9, 56, 24]
lista2 = ['Gustavo', 'Ellen', 'Amora', 'Pretinha', 'Catita']

def swap(lista):
    leng = len(lista)
    
    last_i = lista[leng - 1]
    first_i = lista[0]
    
    lista[0] = last_i
    lista[leng - 1] = first_i
    
    return lista

print(swap(lista2)) 