nome = input("Digite o nome do cliente: ")
valor = float(input("Digite o valor da compra do cliente "))

def calcular_desconto(valor):   
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.10
    else:
        return valor * 0.20
    
valor_desconto = calcular_desconto(valor)

def calcular_valor_final (valor_desconto,valor):
    conta = valor - valor_desconto
    return conta

valor_final = calcular_valor_final(valor_desconto, valor)

resposta = f"\nCliente: {nome}\nValor da compra: {valor}\nDesconto: {valor_desconto}\nValor final: {valor_final} "

print(resposta)
