# ============================================
# Programa: Conversor de Temperatura
# Objetivo: Converter temperaturas entre
#           Celsius, Fahrenheit e Kelvin
# Linguagem: Python
# ============================================

# Entrada de dados
temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

# Conversão para Celsius (base)
if origem == "C":
    temp_c = temperatura
elif origem == "F":
    temp_c = (temperatura - 32) * 5 / 9
elif origem == "K":
    temp_c = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Conversão de Celsius para destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9 / 5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

# Exibição do resultado
print("\nConversor de Temperatura")
print("------------------------")
print(f"Temperatura original: {temperatura}°{origem}")
print(f"Temperatura convertida: {resultado:.2f}°{destino}")

"""
Exemplo de execução:

Digite a temperatura: 25
Unidade de origem (C, F ou K): C
Unidade de destino (C, F ou K): F

Conversor de Temperatura
------------------------
Temperatura original: 25.0°C
Temperatura convertida: 77.00°F
"""
