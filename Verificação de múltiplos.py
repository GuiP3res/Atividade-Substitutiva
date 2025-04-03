numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
  print(f"{numero} é múltiplo de 3 e 5.")
else:
  print(f"{numero} não é múltiplo de 3 e 5.")