# Mostrar qual letra aparece mais vezes nesse paragrafo

frase = 'A mouse (pl: mice) is a small rodent. Characteristically, mice are known to have a pointed snout, small rounded ears, a body-length scaly tail, and a high breeding rate. The best known mouse species is the common house mouse (Mus musculus). Mice are also popular as pets. In some places, certain kinds of field mice are locally common. They are known to invade homes for food and shelter.'
    
i = 0
lista_de_letras = []
letra_com_mais = ''
qtde_letra_com_mais = 0

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual != ' ':
        quantas_vezes_apareceu = frase.count(letra_atual)
        if quantas_vezes_apareceu > qtde_letra_com_mais:
            letra_com_mais = letra_atual
            qtde_letra_com_mais = frase.count(letra_atual) 
    
    i += 1

print(f'A letra que mais apareceu foi "{letra_com_mais}", com {qtde_letra_com_mais} aparições')
