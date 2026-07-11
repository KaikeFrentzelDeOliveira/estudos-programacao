nome = input("Digite o nome do fucionário: ")
salario = float(input("Digite o salario do funcionário: "))
anos = int(input("Digite quantos anos de empresa tem esse funcionário: "))

def calcular_aumento(salario,anos):
    if anos < 2:
        return salario * 0.05
    elif anos >= 2 and anos < 5:
        return salario * 0.10
    else:
        return salario * 0.20

aumento = calcular_aumento(salario,anos)

def calcular_novo_salario(salario,aumento):
    conta = aumento + salario
    return conta

salario_final = calcular_novo_salario (salario,aumento)

resposta = f"\nFuncionário: {nome}\nSalário atual: {salario}\nTempo de empresa: {anos} Anos\nValor do aumento: {aumento}\nNovo salário: {salario_final}"

print(resposta)