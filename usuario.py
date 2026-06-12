# usuarios.py
class Usuarios:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def cadastro(self):
        print(f'O Seu nome :{self.nome} e sua idade : {self.idade}')

c=Usuarios('carlos',45)
c.cadastro()        