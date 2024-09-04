def calcular_area_triangulo(p_base, p_altura):
    p_area = (p_base * p_altura)/2
    return p_area

base = float(input("Digite a base do triangulo: "))
altura = float(input("Digitea altura do triangulo: "))
area = calcular_area_triangulo(base, altura)
print("A área do triângulo é:", area)
