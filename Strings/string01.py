palavra1 = str(input("Digite uma string: "))
palavra2 = str(input("Digite outra string: "))
tam1 = (len(palavra1))
tam2 = (len(palavra2))
CompT = "null"
CompC = "null"
if tam1 == tam2:
    CompT = "As duas strings são de tamanhos iguais"
else:
    CompT = "As duas strings são de tamanhos diferentes"
if palavra1 == palavra2:
    CompC = "As duas strings têm conteúdos iguais"
else:
    CompC = "As duas strings têm conteúdos diferentes"
print(tam1)
print(tam2)
print(CompT)
print(CompC)
print("FIM")

              
