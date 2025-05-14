from flask import Flask, render_template

app = Flask(__name__)


@app.route("/dashboard_aluno")
def dashboard_aluno():
    saldo_scoins = 100  # Exemplo: saldo inicial
    desafios = ["Entregar trabalho antecipado (+20 SCoins)",
                "Participação em aula (+10 SCoins)", "Ajudar um colega (+15 SCoins)"]
    recompensas = ["Caneta personalizada - 50 SCoins",
                   "Hora extra no laboratório - 100 SCoins", "Desconto na mensalidade - 500 SCoins"]
    return render_template("dashboard_aluno.html", scoins=saldo_scoins, desafios=desafios, recompensas=recompensas)


if __name__ == "__main__":
    app.run(debug=True)
