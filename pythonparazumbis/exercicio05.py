preco = float(input("Preço: "))
desconto = float(input("Desconto%: "))

valor_do_desconto = preco * desconto / 100
valor_a_pagar = preco - valor_do_desconto

print(f"Desconto: R$ {valor_do_desconto:.2f}")
print(f"Total a pagar: R$ {valor_a_pagar:.2f}")
