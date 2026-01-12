"""
Calculadora de Consumo de Combustível
Consumo médio de combustível de um veículo.
Dados:
- Distância percorrida: 300 km
- Combustível gasto: 25 litros
"""

# Este programa calcula quantos quilômetros o veículo percorre por litro de combustível.

# -----------------------------
# Dados da viagem
# -----------------------------
distancia_percorrida = 300      # km
combustivel_gasto = 25          # litros

# -----------------------------
# Cálculo do consumo médio
# -----------------------------
consumo_medio = round(distancia_percorrida / combustivel_gasto, 2)

# -----------------------------
# Valor final calculado
# -----------------------------
# Consumo médio: 12.00 km/l

# -----------------------------
# Saída clara no terminal
# -----------------------------
print("Calculadora de Consumo de Combustível")
print("------------------------------------")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
