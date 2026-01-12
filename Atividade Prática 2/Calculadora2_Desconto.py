"""
Calculadora de Desconto
Um programa que calcula o desconto em uma loja.
- Nome do produto: "Camiseta"
- Preço original: R$ 50.00
- Porcentagem de desconto: 20%
"""

# -----------------------------
# Dados de entrada
# -----------------------------
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# -----------------------------
# Cálculos
# -----------------------------
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# -----------------------------
# Valor final calculado
# -----------------------------
# Valor do desconto: R$ 10.00
# Preço final: R$ 40.00

# -----------------------------
# Saída clara no terminal
# -----------------------------
print("Calculadora de Desconto")
print("-----------------------")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
