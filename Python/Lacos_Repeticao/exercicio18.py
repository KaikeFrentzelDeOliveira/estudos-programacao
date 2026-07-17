while True:

    print("===== MENU =====")
    print("1 - Dizer Olá")
    print("2 - Mostrar seu nome")
    print("3 - Sair\n")
    
    numero = int(input("Escolha uma opção: "))

    if numero == 1:
        print("\nOlá!")
    elif numero == 2:
        print ("Kaike Frentzel De Oliveira")
    elif numero == 3:
        break
    else:
        print("Opção inválida!")


