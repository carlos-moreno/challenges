a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a <= b and a <= c:
    print(f"Maior: {a}")
elif b <= c:
    print(f"Maior: {b}")
else:
    print(f"Maior: {c}")
