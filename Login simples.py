usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1234":
  print("Acesso permitido")
else:
  print("Acesso negado")