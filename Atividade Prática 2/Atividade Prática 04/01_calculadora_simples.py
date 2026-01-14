# ============================================
# Programa: Calculadora Simples
# Objetivo: Realizar operações básicas (+, -, *, /)
# Linguagem: Python
# ============================================

def ler_numero(mensagem):
    """Lê um número real com validação (não aceita letras)."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Erro: digite um número válidor.")


# O programa continua solicitando entradas até que uma operação válida seja realizada com sucesso.
while True:
    # -----------------------------
    # Entrada de dados (com validação)
    # -----------------------------
    numero1 = ler_numero("\nDigite o primeiro número: ")
    numero2 = ler_numero("Digite o segundo número: ")

    # -----------------------------
    # Entrada da operação (repete até ser válida)
    # -----------------------------
    while True:
        # Trecho incluído (sem alteração)
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            print("Soma")
        elif operacao == "-":
            print("Subtração")
        elif operacao == "*":
            print("Multiplicação")
        elif operacao == "/":
            print("Divisão")
        else:
            print("Erro: operação inválida.")

        # Validação da operação
        if operacao not in ["+", "-", "*", "/"]:
            print("\nOperação inválida. Tente novamente.\n")
            continue

        # Tratamento de divisão por zero
        if operacao == "/" and numero2 == 0:
            print("\nVocê dividiu por zero, favor tentar novamente.")
            trocar = input("Deseja trocar os números? (S/N): ").strip().upper()

            if trocar == "S":
                # Volta para pedir os números novamente
                break
            else:
                print("Então escolha outra operação.\n")
                continue

        # Se chegou aqui, a operação é válida
        break

    # Se escolheu trocar números por causa de divisão por zero, volta pro começo (pede números)
    if operacao == "/" and numero2 == 0:
        continue

    # -----------------------------
    # Processamento (operação válida)
    # -----------------------------
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    else:  # operacao == "/"
        resultado = numero1 / numero2

    # -----------------------------
    # Saída clara no terminal
    # -----------------------------
    print("\nCalculadora Simples")
    print("-------------------")
    print(f"Resultado: {numero1} {operacao} {numero2} = {resultado:.2f}")

    # Operação realizada com sucesso: encerra o programa
    break

# Comentário com valor final esperado (exemplo)
# Entrada: 12 e 4, operação /
# Saída: Resultado: 12.00 / 4.00 = 3.00
