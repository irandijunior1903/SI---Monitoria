Num = str(input("Digite um valor de 0 até 99: "))
Leitura = len(Num)
Extenso = ["Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa"]
while Leitura != 1 and Leitura != 2:
    Num = str(input("Valor inválido, Digite um valor de 0 até 99: "))
    Leitura = len(Num)   
if Leitura == 1:
    Num = Extenso[Num]
elif Leitura == 2:
    if Num[0] == "1" and Num[1] == "0":
        Num = Extenso[Num]
    elif Num[0] == "1":
        Num = Extenso[Num]

    elif Num[0] == "2" and Num[1] == "0":
        Num = Extenso[20]
    elif Num[0] == "2":
        Num = Extenso[20] + " e " + Extenso[int(Num[1])]

    elif Num[0] == "3" and Num[1] == "0":
        Num = Extenso[21]
    elif Num[0] == "3":
        Num = Extenso[21] + " e " + Extenso[int(Num[1])]

    elif Num[0] == "4" and Num[1] == "0":
        Num = Extenso[22]
    elif Num[0] == "4":
        Num = Extenso[22] + " e " + Extenso[int(Num[1])]

    elif Num[0] == "5" and Num[1] == "0":
        Num = Extenso[23]
    elif Num[0] == "5":
        Num = Extenso[23] + " e " + Extenso[int(Num[1])]

    elif Num[0] == "6" and Num[1] == "0":
        Num = Extenso[24]
    elif Num[0] == "6":
        Num = Extenso[24] + " e " + Extenso[int(Num[1])]

    elif Num[0] == "7" and Num[1] == "0":
        Num = Extenso[25]
    elif Num[0] == "7":
        Num = Extenso[25] + " e " + Extenso[int(Num[1])]

    elif Num[0] == "8" and Num[1] == "0":
        Num = Extenso[26]
    elif Num[0] == "8":
        Num = Extenso[26] + " e " + Extenso[int(Num[1])]
        
    elif Num[0] == "9" and Num[1] == "0":
        Num = Extenso[27]
    elif Num[0] == "9":
        Num = Extenso[27] + " e " + Extenso[int(Num[1])]

print(Num)
print("FIM")
