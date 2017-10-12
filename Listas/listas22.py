Lista= []
Cont = [0,0,0,0]
Soma = 0
while True:
  IdentMouse = int(input("Digite o número de indentificação do mouse: "))
  if IdentMouse == 0:
      break
  print("1 - Para troca da esfera")
  print("2 - Para limpeza")
  print("3 - Para troca do cabo ou conector")
  print("4 - Para quebra ou inutilizado")
  TipoDef = int(input("Digite o tipo de defeito: "))
  Lista.append([IdentMouse,TipoDef])
while len(Lista) > 0:
 for a,b in enumerate(Lista):
     Aux = 0
     L = Lista[:]
     for c,d in enumerate(L):
        if b[1] == d[1] :
           Aux += 1
           Lista.remove(d)
     Soma += Aux
     if Aux > 0:
        if b[1] == 1:
           Cont[0] = Aux
        elif b[1] == 2:
           Cont[1] = Aux
        elif b[1] == 3:
           Cont[2] = Aux
        elif b[1] == 4:
           Cont[3] = Aux
MediaUm = Cont[0] / Soma
MediaDois = Cont[1] / Soma
MediaTres = Cont[2] / Soma
MediaQuatro = Cont[3] / Soma
print("Quantidade de mouses: {}".format(len(Lista)))
print("Para troca de esfera : {} mouses que equivale à {:.2f}% do total de entradas!". format(Cont[0],MediaUm))
print("Para limpeza: {} mouses que equivalem à {:.2f}% do total de entradas!". format(Cont[1],MediaDois))
print("Para troca do cabo ou conector: {} mouses que equivalem à {:.2f}% do total de entradas!". format(Cont[2],MediaTres))
print("Para quebra ou inutilizado: {} mouses que equivalem à {:.2f}% do total de entradas!". format(Cont[3],MediaQuatro))
print("FIM")
