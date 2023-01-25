alunos = []

for al in range(0,3):
    nome = str(input('Nome do aluno:\n'))
    media = float(input('Média do aluno:\n'))
    
    alunos.append({'nome':nome, 'media':media})
    
for al in alunos:
    print('O aluno {} tem média de {}'.format(al['nome'], al['media']))