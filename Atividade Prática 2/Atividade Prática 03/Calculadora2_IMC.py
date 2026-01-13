# ============================================
# Programa: Calculadora de IMC
# Objetivo: Calcular o Índice de Massa Corporal
# ============================================

# Entrada de dados
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibição dos resultados
print("\nCalculadora de IMC")
print("------------------")
print(f"Peso informado: {peso} kg")
print(f"Altura informada: {altura} m")
print(f"IMC calculado: {imc:.2f}")
print(f"Classificação: {classificacao}")

"""
Saída esperada (exemplo):

Digite o peso (em kg): 70
Digite a altura (em metros): 1.75

Calculadora de IMC
------------------
Peso informado: 70.0 kg
Altura informada: 1.75 m
IMC calculado: 22.86
Classificação: Peso normal
"""
