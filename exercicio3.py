alunos = {}
nota = []
for i in range(5):
    nomeAluno  = input('Insira o nome do aluno desejavel')
    if nomeAluno == '':
        break
    for a in range(3):
        notaAluno = float(input('Insira a nota{a} do aluno aqui'))
        nota.append(notaAluno)
    media = notaAluno/3
    alunos[nomeAluno] = media
print(alunos)
