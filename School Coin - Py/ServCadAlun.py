from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/cadastro", methods=["POST"])
def cadastro():
    matricula = request.form["matricula"]
    email = request.form["email"]
    senha = request.form["senha"]

    # Simulação de armazenamento (futuro: banco de dados)
    with open("usuarios.txt", "a") as file:
        file.write(f"{matricula},{email},{senha}\n")

    return redirect("/confirmacao")


if __name__ == "__main__":
    app.run(debug=True)
