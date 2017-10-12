cont = 0
def quantDigitos(num):
	num = str(num)
	global cont
	for i in num:
	    cont += 1
	return cont
num = int(input("Digite o numero para saber a quantidade: "))
print("Quantidade de Digitos de um numero: {}".format(quantDigitos(num)))
print("FIM")
