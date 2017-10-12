Palavra =str.lower(input("Digite sua string: "))
leitura = len(Palavra)
EspaçosB =  0
A = 0
E = 0
I = 0
O = 0
U = 0
Espaço =  '  '
for i in range(leitura):
    if (Palavra [i] =="a"):
        A +=  1
        
    elif (Palavra [i] =="e"):
        E +=  1

    elif (Palavra [i] =="i"):
        I +=  1
        
    elif (Palavra [i] =="o"):
        O +=  1

    elif (Palavra [i] =="u"):
        U +=  1

    if (Palavra [i] == Espaço):
        EspaçosB +=  1
print ("A frase {} possui {} espaços em branco.". format(Palavra, EspaçosB))
print ("{} vogais A e {} vogais E.". format(A, E))
print ("{} vogais I e {} vogais O.". format(I, O))
print ("{} vogais U.". format(U))
print("FIM")
        
