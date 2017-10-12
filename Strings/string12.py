corrigir = "3"
numero = input("Digite um número de telefone fixo: ")
numero = numero.replace("-","")
if len(numero) == 7:
    print(numero)
    print("Este número de telefone possuí sete dígitos, vou acrescentar o 3 na frente.")
    fixo = corrigir + numero
print(fixo)
print("FIM")



              
        
               
