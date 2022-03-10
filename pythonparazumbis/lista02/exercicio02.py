from calendar import isleap

a = int(input("Ano: "))
if isleap(a):
    print("Bissexto")
else:
    print("Não é bissexto")
