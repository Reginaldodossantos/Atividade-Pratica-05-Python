# ============================================
# Programa: Conversor de Moeda
# Objetivo: Calcular e exibir valores convertidos
#           de reais para dólar e euro
# ============================================

# Valor em reais
valor_reais = 100.00

# Taxas de conversão
taxa_dolar = 5.20
taxa_euro = 6.15

# Cálculo das conversões
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibição dos resultados arredondados para duas casas decimais
print("Conversor de Moeda")
print("------------------")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: US$ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}")

# ============================================
# Saída final do programa
# ============================================
# Conversor de Moeda
# ------------------
# Valor em reais: R$ 100.00
# Valor em dólares: US$ 19.23
# Valor em euros: € 16.26
