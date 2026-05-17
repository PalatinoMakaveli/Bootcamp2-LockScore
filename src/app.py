from flask import Flask, render_template, request
from password_checker import check_password_strength
from services.hudsonrock_service import check_email

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None
    senha = ""

    email = ""
    breach_result = None
    risk_level = None

    if request.method == "POST":

        senha = request.form.get("senha", "")
        email = request.form.get("email", "")

        # Verificação da força da senha
        if senha:
            resultado = check_password_strength(senha)

        # Verificação de credenciais comprometidas
        if email:

            api_result = check_email(email)


            stealers = api_result.get("stealers", [])

            if not stealers:

                breach_result = "Nenhuma ameaça encontrada."
                risk_level = "BAIXO"

            else:

                breach_result = (
                    f"{len(stealers)} ameaça(s) encontrada(s)."
                )

                risk_level = "CRÍTICO"

    return render_template(
        "index.html",
        resultado=resultado,
        senha=senha,
        email=email,
        breach_result=breach_result,
        risk_level=risk_level
    )


if __name__ == "__main__":
    app.run()
