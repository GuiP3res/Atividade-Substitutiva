usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
tentativas = 1

while (usuario != "admin" or senha != "1234") and tentativas < 3:
  print("Nome de usuário ou senha incorretos. Tente novamente.")
  usuario = input("Digite o nome de usuário: ")
  senha = input("Digite a senha: ")
  tentativas += 1

if usuario == "admin" and senha == "1234":
  print("Acesso permitido.")
else:
  print("Acesso bloqueado.")