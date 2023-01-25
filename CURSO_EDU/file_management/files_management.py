# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

file_path = 'my_new_file.txt'

with open(file_path, 'w') as file:
    print('Arquivo aberto para write')
    file.write('Arquivo aberto e inserida esse frase.')
    print('Arquivo fechado')
    
with open(file_path, 'a') as file:
    print('Arquivo aberto para append.')
    file.write('\nNova linha adicionada.')
    print('Arquivo fechado.')

with open(file_path, 'a') as file:
    file.write('\nSegunda linha adicionada.')