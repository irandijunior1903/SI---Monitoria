Data = [["Janeiro",31],["Fevereiro",28],["Março",31],["Abril",30],["Maio",31],["Junho",30],["Julho",31],["Agosto",31],["Setembro",30],["Outubro",31],["Novembro",30],["Dezembro",31]]
def mesExtenso(Mes):
    L = []
    if Mes >= 1 and Mes <= 12:
        return Data[Mes-1][0]
    else:
        return Null
Dia = int(input("Digite o dia: "))
Mes = int(input("Digite o mês: "))
Ano = int(input("Digite o ano: "))
if Dia >= 1 and Mes >= 1 and Mes <= 12 and Ano >= 0:
    print("{} de {} de {}.". format(Dia,mesExtenso(Mes),Ano))
print("FIM")
