def numeroRepetir(num):
    for i in range(num+1):
            for j in range(i):
                print(i, end=" ")
            print()
num = int(input("Digite um número: "))
numeroRepetir(num)
print("FIM")
