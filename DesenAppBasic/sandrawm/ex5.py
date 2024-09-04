def converter_polegadas_para_cm(p_polegadas):
    p_cm = p_polegadas * 2.54
    return p_cm

polegadas = float(input("Digite o valor em polegadas: "))
cm = converter_polegadas_para_cm(polegadas)
print("O valor em centímetros é:", cm)