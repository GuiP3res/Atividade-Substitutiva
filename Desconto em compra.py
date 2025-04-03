valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
  desconto = valor_compra * 0.1
  valor_final = valor_compra - desconto
  print(f"Desconto aplicado: R$ {desconto:.2f}")
  print(f"Valor final: R$ {valor_final:.2f}")
else:
  print("Nenhum desconto aplicado.")