n = int(input("Número: "))
k = 1
divisores = 0

while k <= n:
    if n % k == 0:
        divisores += 1
    k += 1

print(divisores == 2)
