"""
1- Classificador de Idade

Programa que solicita a idade de vários usuários e classifica cada um
em uma das seguintes categorias:

- Criança (0-12 anos)
- Adolescente (13-17 anos)
- Adulto (18-59 anos)
- Idoso (60 anos ou mais)
"""

# Laço para permitir a entrada de vários usuários
while True:
    # Solicita a idade do usuário
    idade = int(input("Digite a idade do usuário: "))

    # Classificação da idade
    if idade >= 0 and idade <= 12:
        classificacao = "Criança"
    elif idade >= 13 and idade <= 17:
        classificacao = "Adolescente"
    elif idade >= 18 and idade <= 59:
        classificacao = "Adulto"
    else:
        classificacao = "Idoso"

    # Saída clara no terminal
    print("\nClassificação de Idade")
    print("----------------------")
    print(f"Idade informada: {idade} anos")
    print(f"Classificação: {classificacao}")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja classificar outro usuário? (s/n): ").lower()

    if continuar != "s":
        print("\nPrograma encerrado.")
        break
