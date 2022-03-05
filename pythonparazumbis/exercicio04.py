salario = float(input("Salário: "))
porcentagem = float(input("Aumento%: "))

aumento = salario * porcentagem / 100
novo_salario = salario + aumento

print(f"Valor do aumento é {aumento:.2f}")
print(f"Novo salário é {novo_salario:.2f}")
