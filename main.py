# Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
# - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
# - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
# - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
# - El programa recibe los siguientes parámetros:
#  - Tipo del Pokémon atacante.
#  - Tipo del Pokémon defensor.
#  - Ataque: Entre 1 y 100.
#  - Defensa: Entre 1 y 100.

def calculate_damage(at_type, def_type, attack, defense):
    if (attack < 1 or attack > 100) or (defense < 1 or defense > 100):
        print("ERROR: Attack or defense has got an incorrect value! It must be between 1 and 100.")
        return None

    types = ["Water", "Fire", "Grass", "Electric"]
    effectiveness = {
        "Water": [0.5, 2, 0.5, 1],
        "Fire": [0.5, 0.5, 2, 1],
        "Grass": [2, 0.5, 0.5, 1],
        "Electric": [2, 1, 0.5, 0.5]
    }

    return 50 * (attack / defense) * effectiveness[at_type][types.index(def_type)]

try:
    print(calculate_damage("Water", "Fire", 50, 30)) # 166.66666666666669
    print(calculate_damage("Water", "Fire", 101, -10)) # Error: values not between 1 and 100
    print(calculate_damage("Fire", "Water", 50, 30)) # 41.66666666666667
    print(calculate_damage("Fire", "Fire", 50, 30)) # 41.66666666666667
    print(calculate_damage("Grass", "Electric", 30, 50)) # 30.0
    print(calculate_damage("Electric", "Normal", 30, 50)) # Error: Normal type not supported
except:
    print("ERROR: Pokemon type not supported!")