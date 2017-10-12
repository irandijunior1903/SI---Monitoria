lista = range(10)
VetorM = []
soma = 0
aux = 0
for i in range(len(lista)):
	soma = 0
	print('Notas do {} aluno'.format(i+1))
	for j in range(4):
		num = float(input('Digite a {} nota: '.format(j+1)))
		soma += num
	media = soma / (j+1)
	VetorM.append(media)
	if media >= 7:
		aux += 1
print('Quantidade de alunos com media maior ou iqual a 7: {}'.format(aux))
print('Medias Totais: {}'.format(VetorM))
print("FIM")
