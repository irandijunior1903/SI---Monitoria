palavra = str(input("Digite uma palavra: "))
for i in range(len(palavra)):
    print(palavra[:i+1:])
print("FIM")
