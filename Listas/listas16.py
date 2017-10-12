Aux = 0
Salario = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],[1000]]
Vendas = float(input("Digite o valor dos protudos vendidos durante a semana: "))
Contador = [0,0,0,0,0,0,0,0,0]
while Vendas != 0:
    Comissao = 200 + (Vendas * 0.09)
    if Comissao < 1000:
        for i in range(0,len(Salario)):
            if Comissao >= Salario[i][0] and x <= Salario[i][1]:
                Contador[i] += 1
            else:
                Contador[8]+=1
        vendas = float(input('Digite o valor da venda: '))
for i in range(9):
    if i < 8:
        print("Salários entre {} e {}.". format(Salario[i][0],Salario[i][1]))
        print("Quantidade de vendedores que ganham neste intervalo é de {}!". format(Contador[i]))
    else:
        print("Salários acima de {}.". format(Salario[8]))
        print("Quantidade de vendedores que ganham neste intervalo é de {}!". format(Contador[8]))
print("FIM")
