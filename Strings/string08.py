palavra = str(input("Digite uma string: "))
inverso = palavra[::-1]
if inverso == palavra:
    print("A string é um palíndromo")
else:
    print("A string não é um palíndromo")
print("FIM")
