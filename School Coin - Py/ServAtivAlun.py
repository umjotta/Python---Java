from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/comentario", methods=["POST"])
def comentario():
    materia = request.form["materia"]
    comentario = request.form["comentario"]

    # Simulação de armazenamento (futuro: banco de dados)
    with open("comentarios.txt", "a") as file:
        file.write(f"{materia}: {comentario}\n")

    return redirect("/atividades_aluno")


if __name__ == "__main__":
    app.run(debug=True)
