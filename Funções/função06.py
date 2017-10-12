def converterHorMin(H,M):
    if H <= 12 and H >= 0 and M >= 0 and M <=60:
        return [H,"Am",M]
    elif H > 12 and H < 23 and M >= 0 and M <=60:
        return [H-12,"Pm",M]
    else:
        return "null"
prosseguir = "sim"
while prosseguir != "não":
    H = int(input("Digite a hora: "))
    M = int(input("Digite os minutos: "))
    Aux = converterHorMin(H,M)
    Hor2412 = Aux[0]
    AmPm = Aux[1]
    M = Aux[2]
    print("{}:{} notado em 12h é: {}:{} {}!". format(H,M,Hor2412,M,AmPm))
    prosseguir = str.lower(input("Deseja continuar a converter (Sim ou Não): "))
print("FIM")
