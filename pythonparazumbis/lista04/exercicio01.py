from random import sample

vetor = sample(range(1, 101), 10)
maior = menor = vetor[0]
k = 1

while k < 10:
    if vetor[k] > maior:
        maior = vetor[k]
    if vetor[k] < menor:
        menor = vetor[k]
    k += 1

print(vetor)
print(f"Menor: {menor}")
print(f"Maior: {maior}")
