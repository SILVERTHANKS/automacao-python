nome = []
idade = []
for i in range(3):
    n = input('Digite o nome:')
    nome.append(n)
    id = int(input("digite a idade:"))
    idade.append(id)
    print(f'Olá, meu nome é {nome[i]} e eu tenho {idade[i]} anos.')
    