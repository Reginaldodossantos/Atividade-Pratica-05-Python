# ============================================
# Programa: Verificador de Ano Bissexto
# Objetivo: Verificar se um ano é bissexto ou não
# ============================================

while True:
    # Entrada de dados
    ano = int(input("\nDigite um ano para verificar se é bissexto: "))

    # Verificação de ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado = "é um ano bissexto"
    else:
        resultado = "não é um ano bissexto"

    # Saída no terminal
    print("\nVerificador de Ano Bissexto")
    print("---------------------------")
    print(f"O ano {ano} {resultado}.")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja verificar outro ano? (S/N): ").upper()
    if continuar != "S":
        print("\nPrograma finalizado.")
        break

# Comentário com valor final esperado 
# Entrada: 2024
# Saída: O ano 2024 é um ano bissexto.
