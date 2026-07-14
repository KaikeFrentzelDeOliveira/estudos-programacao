nome = input("Digite o nome do cliente: ")
horas = int(input("Digite a quantidade de horas estacionado: "))
vip = input("O cliente é VIP: ")

def calculuar_valor_hora(horas):
    if horas <= 2:
        return 8
    elif horas <= 5:
        return 6
    else:
        return 5
    
valor_hora = calculuar_valor_hora(horas)

def valor_original (valor_hora,horas):
    return valor_hora * horas;

mostra_valor_original = valor_original (valor_hora,horas)

def calcular_desconto (vip):
    if vip == ("S"):
        return 0.80
    elif vip == ("N"):
        return 1.00
    else:
        return ("ERRO")

valor_desconto = calcular_desconto(vip)

def calcular_valor_final(valor_original, multiplicador):
    return valor_original * multiplicador
    
valor_final = calcular_valor_final(mostra_valor_original,valor_desconto)
    
def mostrar_desconto (valor_desconto):
    if valor_desconto == 0.80:
        return ("20% De desconto")
    elif valor_desconto == 1:
        return ("0% De desconto")
    else:
        return("ERRO")
    
desconto = mostrar_desconto (valor_desconto)

resposta = (f"\nNome: {nome}\nHoras: {horas}\nValor Original:{mostra_valor_original}\nDesconto: {desconto}\nValor Final: {valor_final}")

print(resposta)