# usuarios.py
class Usuarios:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'{self.nome} - {self.idade} anos'


def cadastro():
    cad = []
    while True:
        nome = input('Digite seu nome: ').strip()
        idade = int(input('Digite sua idade: '))
        usuario = Usuarios(nome, idade)
        cad.append(usuario)

        continuar = input('Deseja cadastrar outro? (s/n): ').lower()
        if continuar != 's':
            break

    print('Lista de usuários cadastrados:')
    for u in cad:
        print(u)


cadastro()
