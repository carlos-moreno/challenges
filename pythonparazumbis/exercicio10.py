cigarros = int(input("Cigarros por dia: "))
anos = int(input("Anos fumados: "))

total_de_cigarros = anos * 365 * cigarros
dias = total_de_cigarros / 144

print(f"Você perdeu {dias:.2f} dias")
