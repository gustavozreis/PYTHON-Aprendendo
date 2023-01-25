'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidades de
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com
erros de índices inexistentes na lista.
'''

lista_de_compras = []

while True:
    chosen_option = input('Escolha uma opção\n[i]nserir, [a]pagar, [l]istar:\n')
    if chosen_option == 'i':
        product = input('Digite o produto:\n')
        lista_de_compras.append(product)
        print('Produto adicionado.\n')
    
    elif chosen_option == 'l':
        if len(lista_de_compras) < 1:
            print('A lista está vazia\n')
        else:
            for index, product in enumerate(lista_de_compras):
                print(index, product)

    elif chosen_option == 'a':
        index_to_erase = input('Escolhe um índice para apagar:\n')
        
        try:
            index_to_erase = int(index_to_erase)
            del lista_de_compras[index_to_erase]
            print('Produto apagado!\n')
        except ValueError:
            print('Por favor, digite um número inteiro:\n')
        except IndexError:
            print('Índice não existe na lista.\n')
        except Exception:
            print('Erro desconhecido.\n')
                                
        
        # while index_to_erase.isdigit() != True or int(index_to_erase) > len(lista_de_compras) -1:
        #     index_to_erase = input('Esse não é um indice válido. digite novamente: ')
        
        # lista_de_compras.pop(int(index_to_erase))
        # print('Produto apagado!')
        
    else:
        print('Por favor, escolha [i], [a] ou [l]\n')