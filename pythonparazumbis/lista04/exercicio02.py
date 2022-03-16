from random import sample

vetor = sample(range(1, 101), 20)
pares = []
impares = []

for x in vetor:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print(vetor)
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
