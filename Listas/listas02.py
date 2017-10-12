L= []
quant = int(input('Informe a quantidade de numeros: '))
for i in range(quant):
        num = int(input('Digite o {} valor: '.format(i+1)))
        L.append(num) 
aux = len(L)
print("Ordem Inversa:")
while 0 < aux:
	print(L[aux-1])
	aux -= 1
print("FIM")
