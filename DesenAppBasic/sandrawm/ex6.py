from datetime import date

def verificar_ano_nascimento(p_idade):
    p_ano_atual = date.today().year
    p_ano_nascimento = p_ano_atual - p_idade
    return p_ano_nascimento


idade= int(input("Digite a idade: "))
ano_nascimento = verificar_ano_nascimento(idade)
print("O ano de nascimento é: ", ano_nascimento)
