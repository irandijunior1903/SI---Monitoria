def inversoNumero(num):
	num = str(num)
	for i in range(len(num),0,-1):
		print(num[i-1],end="")
	print()
num = int(input("Digite o numero: "))
print("Inverso: ",end="")
inversoNumero(num)
print("FIM")

