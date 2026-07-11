nome = input("Digite o seu nome: ")
n1 = float(input("Digite a nota 01: "))
n2 = float(input("Digite a nota 02: "))

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

media = calcular_media(n1, n2)

def verificar_situacao(media):
    if media >= 6:
        return "Aprovado!"
    else:
        return "Reprovado!"

situacao_final = verificar_situacao(media)

resposta = f"O aluno {nome} ficou com uma média de {media:.2f} e foi {situacao_final}"

print(resposta)