from flask import *

users = {
    "joao@teste": "password1",
}

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email_login")
        password = request.form.get("pass_login")
        
        if email in users and users[email] == password:
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))  

    return render_template("login.html")  

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
