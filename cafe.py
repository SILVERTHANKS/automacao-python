# cafeteira

cafe = input('Deseja café (s/n)? ').lower().strip()

if cafe == "s":
    print("Opções:")
    print("1 - Café com leite")
    print("2 - Café puro")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Café com leite")
    elif opcao == "2":
        print("Café puro")
    else:
        print("Opção inválida!")
else:
    print("Até a próxima!")