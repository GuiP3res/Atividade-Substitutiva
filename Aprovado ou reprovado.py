nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência do aluno (%): "))

if nota >= 6 and frequencia >= 75:
  print("Aprovado")
else:
  print("Reprovado")