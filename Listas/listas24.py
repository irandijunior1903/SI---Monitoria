from random import randrange
L = []
Numeros = [0,0,0,0,0,0]
for a in range(100):
    dado = randrange(1,7)
    L.append(dado)
    Numeros[dado-1] += 1
for b,face in enumerate(Numeros):
    print("{} dados de face número {}.". format(face,b+1))
print("FIM")
