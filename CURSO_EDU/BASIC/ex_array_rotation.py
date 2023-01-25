# Example:

# lista = [1, 2, 3, 4, 5, 6, 7]
# lista_left_rotation_by_1 = [2, 3, 4, 5, 6, 7, 1]

lista = [1, 2, 3, 4, 5, 6, 7, 8]

def rotate(lista, times_to_rotate, rotation_direction):
    
    new_list = list(lista)
    temp_list = list(lista)
    
    if rotation_direction == 'left':
        for rotation in range(times_to_rotate):
            for i, item in enumerate(temp_list):
                if i == len(lista) - 1:
                    new_list[-1] = temp_list[0]
                else:
                    new_list[i] = temp_list[i+1]                    
            temp_list = list(new_list)
    
    else:
        for rotation in range(times_to_rotate):
            for i, item in enumerate(temp_list):
                if i == 0:
                    new_list[0] = temp_list[-1]
                else:
                    new_list[i] = temp_list[i-1]
            temp_list = list(new_list)
              
    return new_list

        
print(rotate(lista, 1, 'right'))
print(rotate(lista, 2, 'right'))
print(rotate(lista, 3, 'right'))
print(rotate(lista, 4, 'right'))