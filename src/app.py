from flask import Flask, render_template, request
from password_checker import check_password_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    senha = ""

    if request.method == "POST":
        senha = request.form["senha"]
        resultado = check_password_strength(senha)

    return render_template("index.html", resultado=resultado, senha=senha)

if __name__ == "__main__":
    app.run(debug=True)