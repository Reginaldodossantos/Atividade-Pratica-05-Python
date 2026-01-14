# ============================================
# Programa: Verificador de Senhas Fortes
# Objetivo: Avaliar a força de uma senha informada pelo usuário
# Regras:
#   - Pelo menos 8 caracteres
#   - Pelo menos 1 número
# Encerramento:
#   - Quando a senha for forte
#   - Ou quando o usuário digitar "sair"
# ============================================

MIN_TAMANHO = 8


def possui_numero(texto: str) -> bool:
    """Retorna True se o texto contiver pelo menos um dígito."""
    return any(char.isdigit() for char in texto)


def validar_senha(senha: str) -> tuple[bool, list[str]]:
    """
    Valida a senha conforme as regras do exercício.
    Retorna:
      - (True, []) se for forte
      - (False, [motivos]) se for fraca
    """
    motivos = []

    if len(senha) < MIN_TAMANHO:
        motivos.append(f"Precisa ter pelo menos {MIN_TAMANHO} caracteres.")

    if not possui_numero(senha):
        motivos.append("Precisa conter pelo menos um número.")

    senha_forte = len(motivos) == 0
    return senha_forte, motivos


def main() -> None:
    """Loop principal do programa."""
    print("Verificador de Senhas Fortes")
    print("Digite uma senha para avaliar. Para sair, digite 'sair'.")
    print("-" * 48)

    while True:
        senha = input("Digite a senha (ou 'sair'): ").strip()

        if senha.lower() == "sair":
            print("Programa encerrado pelo usuário.")
            return

        forte, motivos = validar_senha(senha)

        if forte:
            print("Senha forte")
            print("Programa encerrado: senha forte cadastrada.")
            return

        print("Senha fraca ❌")
        for motivo in motivos:
            print(f"- {motivo}")
        print("Tente novamente.\n")


if __name__ == "__main__":
    main()

"""
Saída esperada (exemplo):

Verificador de Senhas Fortes
Digite uma senha para avaliar. Para sair, digite 'sair'.
------------------------------------------------
Digite a senha (ou 'sair'): abc
Senha fraca 
- Precisa ter pelo menos 8 caracteres.
- Precisa conter pelo menos um número.
Tente novamente.

Digite a senha (ou 'sair'): SenhaForte1
Senha forte 
Programa encerrado: senha forte cadastrada.
"""
