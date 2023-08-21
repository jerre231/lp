import pandas as pd
import os, platform

def clear_screen():
    os_name = platform.system()

    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class Agenda():
    def __init__(self):
        self.numero = {}  # Inicialize o dicionário vazio

    def inserir(self):
        nome_inserir = input("Digite o nome: ")
        numero_inserir = input("Digite o número: ")
        self.numero[nome_inserir] = numero_inserir
        self.salvar()

    def editar(self):
        nome_editar = input("Digite o nome do contato para editar: ")
        novo_numero = input(f"Digite o novo número para {nome_editar}: ")

        with open('dic.txt', 'r+') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)  # Voltar ao início do arquivo

            for linha in linhas:
                if linha.startswith(nome_editar + ":"):
                    arquivo.write(f"{nome_editar}:{novo_numero}\n")
                else:
                    arquivo.write(linha)
    
    def remover(self):
        nome_remover = input("Digite o nome do contato para remover: ")

        with open('dic.txt', 'r+') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)  # Voltar ao início do arquivo
            arquivo.truncate(0)  # Limpar o arquivo

            for linha in linhas:
                if not linha.startswith(nome_remover + ":"):
                    arquivo.write(linha)

    def imprimir(self):
        df = pd.read_csv('dic.txt', delimiter=':', header=None, names=['Nome', 'Número'])
        print(df.to_string(index=False))

    def salvar(self):
        with open('dic.txt', 'a') as dicionario:
            for nome, numero in self.numero.items():
                linha = f"{nome}: {numero}\n"
                dicionario.write(linha)
        self.numero = {}

    def sair(self):
        self.salvar()
        print("Agenda salva no arquivo dic.txt")

# Código principal
agenda = Agenda()

while True:
    print("\nOpções:")
    print("1 - Inserir contato")
    print("2 - Editar número")
    print("3 - Remover contato")
    print("4 - Imprimir agenda")
    print("5 - Sair")
    escolha = input("Escolha uma opção: ")
    clear_screen()

    if escolha == '1':
        agenda.inserir()
    elif escolha == '2':
        agenda.editar()
    elif escolha == '3':
        agenda.remover()
    elif escolha == '4':
        agenda.imprimir()
    elif escolha == '5':
        agenda.sair()
        break
    else:
        print("Opção inválida")
