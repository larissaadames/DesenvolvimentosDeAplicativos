def calcular_potencial(p_base, p_expoente):
    p_resultado = p_base ** p_expoente
    return p_resultado

base = float(input("Digite a base: "))
expoente = int(input("Digite o expente: "))
resultado = calcular_potencial(base, expoente)
print("O resultado da potenciação é:", resultado)