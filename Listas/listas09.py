lista = list(range(10))
L = lista
quadrad = 0
for i in range(len(lista)):
	L[i] = int(input('Digite o número {}: '.format(i+1)))
	quadrad += L[i]**2
print('Soma dos quadrados dos números {} '.format(quadrad))
print("FIM")
