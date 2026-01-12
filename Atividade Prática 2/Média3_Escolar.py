"""
Calculadora de Média Escolar
Programa que calcula a média escolar de um aluno.
- Nota 1: 7.5
- Nota 2: 8.0
- Nota 3: 6.5
"""

# -----------------------------
# Notas do aluno
# -----------------------------
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# -----------------------------
# Cálculo da média
# -----------------------------
media = round((nota1 + nota2 + nota3) / 3, 2)

# -----------------------------
# Valor final calculado
# -----------------------------
# Média final: 7.33

# -----------------------------
# Saída clara no terminal
# -----------------------------
print("Calculadora de Média Escolar")
print("----------------------------")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}")
