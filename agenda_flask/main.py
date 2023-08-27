from flask import *                                             #TODO: trocar todos os txt's por SQL
import pandas as pd                                             #TODO: uma agenda diferente para cada usuário
from classes import Agenda, Users                               #TODO: botão de voltar a o login na pagina da agenda
                                                                #TODO: implementar alguma mecanismo de segurança (tentar colocar id de cada user no endereço da agenda)
#inicialização do app_Flask
app = Flask(__name__)

#Declaração dos objeto 
agenda = Agenda()
user = Users()

#Pagina de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email_login")
        password = request.form.get("pass_login")

        '''
        if email in users and users[email] == password:
            return redirect(url_for("imprimir"))'''
        
        with open('users.txt', 'r+') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)

            for linha in linhas:
                if not linha == (email + ": " + password):
                    return redirect(url_for("imprimir"))
                
                else:
                    return redirect(url_for("login"))

    return render_template("login.html")

#Página home (inútil até então)
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

#Método usado para obter os requests dentro da box da agenda
@app.route("/box", methods=["GET", "POST"])
def box():
    nome = request.form.get("nome")
    numero = request.form.get("numero")
    opc = request.form.get("opc")

    if opc == "insert":
        agenda.inserir(nome, numero)
    elif opc == "remove":
        agenda.remover(nome, numero)
    
    return redirect(url_for("imprimir"))

#Pagina da agenda de fato
@app.route("/imprimir")
def imprimir():
    df = pd.read_csv('data.txt', delimiter=':', header=None, names=['Nome', 'Número'])
    tabela_html = df.to_html(classes='table table-striped', index=False)
    
    return render_template("home.html", tabela_html=tabela_html)

#Pagina de cadastro (igual a de login)
@app.route("/pagina_de_cadastro", methods=["GET", "POST"])
def pagina_de_cadastro():
    if request.method == "POST":
        email = request.form.get("email_cadastro")
        password = request.form.get("pass_cadastro")
        user.inserir_user(email, password)
        return redirect(url_for("login")) 

    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run()
