print('CAIXA ELETRÔNICO'.center(32,'*'))
saldo = 1000
senha = '140381'
tentativas = 0
limite_tentativas = 3

while True:
    chave = input('Digite sua senha: ').strip()
    if chave == senha:
        print('Acesso concedido.') 
        while True:
            print(''' 
            Opções de Entrada 
            (1) - Saldo
            (2) - Saque
            (3) - Depósito
            (4) - Sair ''')    
            
            opcoes = input('Digite sua opção: ')
            if opcoes == '1':
                print(f'Seu saldo é R$ {saldo:.2f}')
            elif opcoes == '2':
                saque = float(input('Digite o valor do saque: '))
                if saque <= saldo:
                    saldo -= saque
                    print(f'Você sacou R$ {saque:.2f}. Saldo atual: R$ {saldo:.2f}')
                else:
                    print('Saldo insuficiente.')
            elif opcoes == '3':
                deposito = float(input('Digite o valor do depósito: '))
                saldo += deposito
                print(f'Depósito realizado. Saldo atual: R$ {saldo:.2f}')
            elif opcoes == '4':
                print('Fim de programa.')
                break
            else:
                print('Opção inválida.')
        break
    else:
        tentativas += 1
        print('Senha incorreta.')
        if tentativas >= limite_tentativas:
            print('Número de tentativas excedido. Cartão bloqueado.')
            break
