# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy
from dados import produtos_modulo

novos_produtos = copy.deepcopy([
    {'nome': produto['nome'], 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in produtos_modulo.produtos
])

# print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key=lambda produto: produto['nome'])


produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key=lambda produto: produto['preco'])

# print(*produtos_ordenados_por_nome, sep='\n')
print(*produtos_ordenados_por_preco, sep='\n')
print(*produtos_modulo.produtos, sep='\n')