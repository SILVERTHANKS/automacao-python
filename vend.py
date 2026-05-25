#criando app para compras 
print('Seja bem vindo'.center(32,"*"))
pedidos = []
escolhar = input('Escolhar seu prato : ').lower().strip()
pedidos.append(escolhar)
print(f'O PRATO ESCOLHIDO FOI {escolhar}')
print(f'Seu Pedidos foram {pedidos}')