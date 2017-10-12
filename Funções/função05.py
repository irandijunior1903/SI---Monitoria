def somaImposto(custo, taxaImposto):
	return custo * (taxaImposto/100) + custo
custo = float(input("Digite o custo: "))
taxaImposto = float(input("Digite o imposto em porcentagem: "))
print(somaImposto(custo, taxaImposto))
print("FIM")
