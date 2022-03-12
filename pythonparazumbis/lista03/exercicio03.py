a = 80_000
b = 200_000
anos = 0

while a <= b:
    a += a * 0.03
    b += b * 0.015
    anos += 1
print(anos)
