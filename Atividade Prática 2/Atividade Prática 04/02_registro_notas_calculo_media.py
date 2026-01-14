"""
Registro de Notas e Cálculo da Média (Turma)

Descrição:
    Programa para registrar notas informadas pelo usuário e calcular a média final da turma.

Regras:
    - O programa solicita notas continuamente até o usuário digitar "fim".
    - Apenas notas no intervalo [0, 10] são aceitas.
    - Entradas inválidas são tratadas com mensagens de erro.
    - Ao final, exibe:
        * total de notas válidas registradas
        * média final com duas casas decimais
"""

from typing import List


def ler_notas() -> List[float]:
    """Lê notas do usuário até que 'fim' seja digitado, validando intervalo e formato."""
    notas: List[float] = []

    while True:
        entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ").strip()

        if entrada.lower() == "fim":
            return notas

        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida. Informe um número entre 0 e 10 ou digite 'fim'.")
            continue

        if 0.0 <= nota <= 10.0:
            notas.append(nota)
            print("Nota registrada.")
        else:
            print("Nota fora do intervalo permitido. Digite um valor entre 0 e 10.")


def calcular_media(notas: List[float]) -> float:
    """Calcula a média aritmética de uma lista de notas. Retorna 0.0 se a lista estiver vazia."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def main() -> None:
    """Função principal do programa."""
    notas = ler_notas()
    total = len(notas)

    if total == 0:
        print("\nNenhuma nota válida foi registrada.")
        return

    media = calcular_media(notas)

    print("\n=== Resultado Final ===")
    print(f"Total de notas válidas: {total}")
    print(f"Média final da turma: {media:.2f}")


if __name__ == "__main__":
    main()
