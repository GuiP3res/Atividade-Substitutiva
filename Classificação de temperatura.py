temperatura = float(input("Digite a temperatura em °C: "))

if temperatura < 15:
  print("Frio")
elif 15 <= temperatura <= 30:
  print("Agradável")
else:
  print("Quente")