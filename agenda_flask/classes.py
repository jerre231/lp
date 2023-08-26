class Users():
    def __init__(self):
        self.temp = {}
    
    def inserir_user(self, nome, passw):
        self.temp[nome] = passw
        self.salvar_user()

    def salvar_user(self):
        with open('users.txt', 'a') as arquivo:
            for nome, passw in self.temp.items():
                linha = f"{nome}: {passw}\n"
                arquivo.write(linha)
        self.temp = {}

class Agenda():
    def __init__(self):
        self.cont = {}
    
    def inserir(self, nome, numero):
        self.cont[nome] = numero
        self.salvar()

    def remover(self, nome):
        with open('data.txt', 'r+') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)
            arquivo.truncate(0)

            for linha in linhas:
                if not linha.startswith(nome + ":"):
                    arquivo.write(linha)

    def salvar(self):
        with open('data.txt', 'a') as arquivo:
            for nome, numero in self.cont.items():
                linha = f"{nome}: {numero}\n"
                arquivo.write(linha)
        self.cont = {}
