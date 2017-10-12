ListaCarros = [["Fusca",9.7],["Gol",11.3],['Uno',13.5],["Vectra",8.1],["Peugeout",10.6]]
Aux = 1000000
print("Comparativo de Consumo de Combustivel")
for i in range(len(ListaCarros)):
    print("Carro nº: {}.". format(i+1))
    print("Nome do veículo: {}.". format(ListaCarros[i][0]))
    print("Consumo (Km por litro): {}.". format(ListaCarros[i][1]))
print("Relatorio Final:")
for i in range(len(ListaCarros)):
    Litro = 1000 / ListaCarros[i][1]
    Pag = Litro * 2.25
    if Litro < Aux:
        Aux = Litro
        Nome = ListaCarros[i][0]
    print("Carro nº: {}, tipo do veículo: {}, Km/L: {}, quantidade de litros se o veículo percorrer 1000Km: {:.2f}, Litros (R$): {:.2f}.". format(i+1,ListaCarros[i][0],ListaCarros[i][1],Litro,Pag))
print("O menor consumo é do veículo: {}". format(Nome))
print("FIM")
