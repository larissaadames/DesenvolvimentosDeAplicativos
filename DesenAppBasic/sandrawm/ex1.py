def calcular_desconto(p_valor , p_desconto):
    p_valor_com_desconto = p_valor - (p_valor*p_desconto)/100
    return p_valor_com_desconto


valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_com_desconto = calcular_desconto(valor, desconto)
print("O valor com desconto é:", valor_com_desconto)