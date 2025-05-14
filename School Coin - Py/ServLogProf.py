from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/login_professor", methods=["POST"])
def login_professor():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if usuario == "professor123" and senha == "senha_professor":  # Simulação
        return redirect("/dashboard_professor")
    else:
        return "Credenciais inválidas!"


if __name__ == "__main__":
    app.run(debug=True)
