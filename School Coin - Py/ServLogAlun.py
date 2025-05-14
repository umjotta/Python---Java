from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    matricula = request.form["matricula"]
    senha = request.form["senha"]

    if matricula == "123456" and senha == "senha123":  # Apenas um exemplo simples
        return redirect("/dashboard")
    else:
        return "Credenciais inválidas!"


if __name__ == "__main__":
    app.run(debug=True)
