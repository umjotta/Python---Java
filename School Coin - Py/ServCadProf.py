from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/cadastro_professor", methods=["POST"])
def cadastro_professor():
    nome = request.form["nome"]
    usuario = request.form["usuario"]
    email = request.form["email"]
    senha = request.form["senha"]

    # Simulação de armazenamento (futuro: banco de dados)
    with open("professores.txt", "a") as file:
        file.write(f"{nome},{usuario},{email},{senha}\n")

    return redirect("/confirmacao_professor")


if __name__ == "__main__":
    app.run(debug=True)
