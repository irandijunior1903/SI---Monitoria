Dia,Mes,Ano = input("Digite sua data de nascimento (DD/MM/AAAA): ").split("/")
while (len(Dia) != 2  or len(Mes) != 2  or len(Ano) != 4):
    print()
    print("Data inválida!")
    Dia,Mes,Ano = input("Digite sua data de nascimento (DD/MM/AAAA): ").split("/")
Calendário = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
print("Você nasceu em {} de {} de {}!". format(Dia,Calendário[int(Mes)-1],Ano))
print("FIM")
