palavra = str(input("Digite uma string: "))
for i in range(len(palavra)):
    print(palavra[0:(len(palavra))-i:1])
print("FIM")
