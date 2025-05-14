from flask import Flask, render_template

app = Flask(__name__)


@app.route("/pessoas")
def pessoas():
    return render_template("pessoas.html")


if __name__ == "__main__":
    app.run(debug=True)
