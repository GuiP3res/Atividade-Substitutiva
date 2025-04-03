import random

def verificar_voto():
    idade = int(input("Digite sua idade: "))
    if idade >= 16:
        print("Você pode votar!")
    else:
        print("Você ainda não pode votar.")

def classificar_temperatura():
    temperatura = float(input("Digite a temperatura em °C: "))
    if temperatura < 15:
        print("Frio")
    elif 15 <= temperatura <= 30:
        print("Agradável")
    else:
        print("Quente")

def login_simples():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == "admin" and senha == "1234":
        print("Acesso permitido")
    else:
        print("Acesso negado")

def verificar_multiplos():
    numero = int(input("Digite um número: "))
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} é múltiplo de 3 e 5.")
    else:
        print(f"{numero} não é múltiplo de 3 e 5.")

def positivo_negativo_zero():
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")

def aprovado_reprovado():
    nota = float(input("Digite a nota do aluno: "))
    frequencia = float(input("Digite a frequência do aluno (%): "))
    if nota >= 6 and frequencia >= 75:
        print("Aprovado")
    else:
        print("Reprovado")

def verificar_feriado():
    dia = input("Digite um dia da semana: ").lower()
    if dia == "sábado" or dia == "domingo":
        print("É feriado!")
    else:
        print("Não é feriado.")

def desconto_compra():
    valor_compra = float(input("Digite o valor da compra: "))
    if valor_compra > 100:
        desconto = valor_compra * 0.1
        valor_final = valor_compra - desconto
        print(f"Desconto aplicado: R$ {desconto:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")
    else:
        print("Nenhum desconto aplicado.")

def sistema_pontuacao():
    pontuacao = int(input("Digite a pontuação do usuário: "))
    if pontuacao >= 90:
        print("Excelente")
    elif pontuacao >= 70:
        print("Bom")
    elif pontuacao >= 50:
        print("Regular")
    else:
        print("Ruim")

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativa = int(input("Adivinhe o número (1 a 10): "))
    while tentativa != numero_secreto:
        if tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
        tentativa = int(input("Tente novamente: "))
    print("Parabéns, você acertou!")

def contagem_progressiva():
    for i in range(1, 11):
        print(i)

def contagem_regressiva():
    i = 10
    while i >= 1:
        print(i)
        i -= 1

def tabuada_5():
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

def numeros_pares():
    for i in range(2, 21, 2):
        print(i)

def soma_numeros():
    soma = 0
    for _ in range(5):
        numero = int(input("Digite um número: "))
        soma += numero
    print(f"A soma dos números é: {soma}")

def adivinhando_senha():
    senha = input("Digite a senha: ")
    while senha != "python123":
        print("Senha incorreta.")
        senha = input("Digite a senha novamente: ")
    print("Senha correta! Acesso permitido.")

def jogo_parar():
    palavra = input("Digite uma palavra: ")
    while palavra.lower() != "parar":
        palavra = input("Digite outra palavra: ")
    print("Programa encerrado.")

def contagem_vogais():
    palavra = input("Digite uma palavra: ").lower()
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    print(f"A palavra tem {contador} vogais.")

def numero_primo():
    numero = int(input("Digite um número: "))
    if numero > 1:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                print(f"{numero} não é primo.")
                break
        else:
            print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

def login_tentativas():
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

def exibir_menu():
    print("\nEscolha um programa:")
    print("1. Verificação de voto")
    print("2. Classificação de temperatura")
    print("3. Login simples")
    print("4. Verificação de múltiplos")
    print("5. Positivo, negativo ou zero")
    print("6. Aprovado ou reprovado")
    print("7. Verificação de feriado")
    print("8. Desconto em compra")
    print("9. Sistema de pontuação")
    print("10. Jogo de adivinhação")
    print("11. Contagem progressiva")
    print("12. Contagem regressiva")
    print("13. Tabuada do 5")
    print("14. Números pares")
    print("15. Soma de números")
    print("16. Adivinhando a senha")
    print("17. Jogo do 'parar'")
    print("18. Contagem de vogais")
    print("19. Número primo")
    print("20. Login com tentativas")
    print("0. Sair")

programas = {
    "1": verificar_voto,
    "2": classificar_temperatura,
    "3": login_simples,
    "4": verificar_multiplos,
    "5": positivo_negativo_zero,
    "6": aprovado_reprovado,
    "7": verificar_feriado,
    "8": desconto_compra,
    "9": sistema_pontuacao,
    "10": jogo_adivinhacao,
    "11": contagem_progressiva,
    "12": contagem_regressiva,
    "13": tabuada_5,
    "14": numeros_pares,
    "15": soma_numeros,
    "16": adivinhando_senha,
    "17": jogo_parar,
    "18": contagem_vogais,
    "19": numero_primo,
    "20": login_tentativas,
}

while True:
    exibir_menu()
    escolha = input("Digite o número do programa desejado: ")
    if escolha == "0":
        break
    programa = programas.get(escolha)
    if programa:
        programa()
    else:
        print("Opção inválida.")
    input("\nPressione Enter para continuar...")