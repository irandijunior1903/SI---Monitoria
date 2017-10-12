def TotalPag(Quantia,Dias):
    if Dias == 0:
        return Quantia
    else:
        return ((Quantia * 0.03) + (Dias * 0.01)* Quantia) + Quantia
Quantia = 1
Aux = 0
Soma = 0
while Quantia != 0:
    Quantia = float(input("Digite o valor da prestação: "))
    Dias = int(input("Digite os dias de atraso no pagamento: "))
    print("Valor a ser pago é de R${:.2f}.". format(TotalPag(Quantia,Dias)))
    Aux += 1
    Soma += TotalPag(Quantia,Dias)    
print("Total de pagamentos foi de {}.". format(Aux))
print("Total arrecadado é de R${:.2f}". format(Soma))
print("FIM")
