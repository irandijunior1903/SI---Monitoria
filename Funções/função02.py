def imprimirNumero(num):
	for i in range(1,num+1):
		for j in range(1,i+1):
			print(j,end=' ')
		print()
num = int(input("Digite um número: "))
imprimirNumero(num)
print("FIM")
