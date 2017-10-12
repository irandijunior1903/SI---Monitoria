lista = list(range(20))
V = []
VetorP = []
VetorI = []
for i in range(len(lista)):
	num = int(input('Informar o {} valor: '.format(i+1)))
	V.extend([num])
	if num % 2 == 0:
		VetorP.append(num)
	else:
		VetorI.extend([num])
print('Vetor: {}'.format(V))
print('Vetor Par: {}'.format(VetorP))
print('Vetor Impar: {}'.format(VetorI))
print("FIM")
