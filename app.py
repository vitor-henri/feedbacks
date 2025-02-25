from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# criando a rota para a pagina principal
@app.route("/", methods=["GET"])
def pag_main():
    return render_template("index.html")

app.run(debug=True, host="0.0.0.0", port=8080)