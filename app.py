from flask import Flask, render_template, request, redirect
import datetime
import 

app = Flask(__name__)

# criando a rota para a pagina principal
@app.route("/", methods=["GET"])
def pag_main():
    return render_template("index.html")

@app.route("/post/mensagem", methods=["POST"])
def post_mensagem():
    # capturando as informações do usuario
    nome_user = request.form.get("nome_user")
    comentario = request.form.get("comentario")
    data_comentario = datetime.datetime.today()

    #cadastrando as informações do usuario no MYSQL (banco de dados)


    return redirect("/")

app.run(debug=True, host="0.0.0.0", port=8080)
