valor = float(input("Valor por hora: "))
horas = int(input("Horas trabalhadas: "))

bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - (ir + inss + sind)

print(f"+Salário Bruto: \t R$ {bruto:.2f}")
print(f"-IR (11%): \t\t\t R$ {ir:.2f}")
print(f"-INSS (8%): \t\t R$ {inss:.2f}")
print(f"-Sindicato (5%): \t R$ {sind:.2f}")
print(f"=Salário Líquido: \t R$ {liquido:.2f}")
