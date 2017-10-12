L = list(range(1,7)) 
L = [0] * 6
Media = [0] * 6
Votos = 0
while True:
    print("Qual o melhor sistema operacional para uso em servidores?")
    print("1 - Windowns")
    print("2 - Unix")
    print("3 - Linux")
    print("4 - Netware")
    print("5 - Mac OS")
    print("6 - Outro")
    Escolha =int(input(": ") )
    if Escolha == 0:
        print("Escolha inválida, Tente novamente!")
        print("Relatório final:")
        break
    else:
        L[Escolha-1] += 1
        Votos += 1
for i in range(len(L)):
	Media[i] = L[i] / Votos*100
print("Windowns: {} votos {:.2f}%". format(L[0],Media[0]))
print("Unix:  -  {} votos  -  {:.2f}%". format(L[1],Media[1]))
print("Linux:  -  {} votos  -  {:.2f}%.". format(L[2],Media[2]))
print("Netware:	-  {} votos  -  {:.2f}%.". format(L[3],Media[3]))
print("Mac OS:  -  {} votos  -  {:.2f}%.". format(L[4],Media[4]))
print("Outro:  -  {} votos  -  {:.2f}%.". format(L[5],Media[5]))
print("Total: {} votos". format(Votos))
print("FIM")
