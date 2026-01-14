# ============================================
# Programa: Analisador de Números Pares e Ímpares
# Objetivo: Classificar números inteiros como pares ou ímpares
# Regras:
#   - Ler números até o usuário digitar "fim"
#   - Informar se cada número é par ou ímpar
#   - Ao final, exibir o total de pares e ímpares
#   - Tratar entradas inválidas com mensagens claras
# ============================================


def tentar_converter_inteiro(texto: str) -> tuple[bool, int | None, str]:
    """
    Tenta converter a entrada para inteiro.
    Retorna (ok, valor, mensagem_erro).
    """
    texto = texto.strip()

    if texto == "":
        return False, None, "Erro: entrada vazia. Digite um número inteiro ou 'fim'."

    try:
        valor = int(texto)
        return True, valor, ""
    except ValueError:
        return False, None, f"Erro: '{texto}' não é um número inteiro válido. Digite um inteiro ou 'fim'."


def classificar_par_impar(numero: int) -> str:
    """Retorna 'par' se o número for par, senão retorna 'ímpar'."""
    return "par" if numero % 2 == 0 else "ímpar"


def main() -> None:
    pares = 0
    impares = 0

    print("Analisador de Números Pares e Ímpares")
    print("Digite números inteiros. Para finalizar, digite 'fim'.")
    print("-" * 52)

    while True:
        entrada = input("Digite um número inteiro (ou 'fim'): ").strip()

        # Encerrar
        if entrada.lower() == "fim":
            break

        # Validar entrada
        ok, numero, erro = tentar_converter_inteiro(entrada)
        if not ok:
            print(erro)
            print()
            continue

        # Classificar e contar
        classificacao = classificar_par_impar(numero)

        if classificacao == "par":
            pares += 1
        else:
            impares += 1

        print(f"O número {numero} é {classificacao}.")
        print()

    # Resultado final
    print("Resultado Final")
    print("--------------")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")


if __name__ == "__main__":
    main()

"""
Saída esperada (exemplo):

Analisador de Números Pares e Ímpares
Digite números inteiros. Para finalizar, digite 'fim'.
----------------------------------------------------
Digite um número inteiro (ou 'fim'): 
Erro: entrada vazia. Digite um número inteiro ou 'fim'.

Digite um número inteiro (ou 'fim'): 10
O número 10 é par.

Digite um número inteiro (ou 'fim'): 7
O número 7 é ímpar.

Digite um número inteiro (ou 'fim'): 7.5
Erro: '7.5' não é um número inteiro válido. Digite um inteiro ou 'fim'.

Digite um número inteiro (ou 'fim'): abc
Erro: 'abc' não é um número inteiro válido. Digite um inteiro ou 'fim'.

Digite um número inteiro (ou 'fim'): fim
Resultado Final
--------------
Total de números pares: 1
Total de números ímpares: 1
"""
