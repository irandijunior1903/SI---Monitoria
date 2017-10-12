VetA = []
VetB = []
VetC = []
for x in range(10):
    VetA.append(int(input("Digite um número inteiro: ")))

for y in range(10):
    VetB.append(int(input("Digite um número inteiro: ")))

for z in range(len(VetA)):
    VetC.append(VetA[z])
    VetC.append(VetB[z])
print(VetC)
print("FIM")
