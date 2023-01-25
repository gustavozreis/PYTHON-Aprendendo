# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

todo_to_print = []
todo_index = 0
can_redo = len(todo_to_print) < 0

def print_list():    
    print()
    print('[### TAREFAS: ###]')
    print()
    if todo_to_print:
        for index in range(todo_index):
            print(todo_to_print[index])
        print()
    else:
        print('Nada a listar.')
        print()

while True:
    print('Comandos: listar, desfazer, refazer.')
    
    comando = input('Digite uma tarefa ou comando: ')
    
    if comando == 'listar':
        print_list()
                
    elif comando == 'desfazer':
        todo_index -= 1
        print_list()        
        
    elif comando == 'refazer':
        if can_redo == False:
            print()
            print('Nada para refazer')
            print()
        else:
            todo_index += 1
            print_list()
        
    elif comando == 'sair':
        break
    
    else:
        todo_to_print = todo_to_print[:todo_index]
        todo_to_print.append(comando)
        todo_index += 1
        print_list()
    