numero = int(input("Digite um número: "))

for i in range (1, numero +1):
    if i %2 == 0:
        print(f"{i}- Par")
    else:
        print(f"{i}- Impar")
