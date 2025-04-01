# Dev by Vitor
from flask import Flask, render_template, request, redirect
from model.coment_controller import Comment
from model.user_controller import User


app = Flask(__name__)

comentarios = []

# criando a rota para a pagina principal
@app.route("/")
def pag_login():
    return render_template("login.html")

@app.route("/post/cadastro", methods=["POST"])
def cadastrar_user():
    
    login = request.form.get("input__user")    
    senha = request.form.get("input__senha")
    nome = request.form.get("input__nome")

    if(User.cadastrar_user(login, senha, nome)):

        return redirect("login.html", login = login, senha = senha, nome = nome)
    
    else:   
        return '<a href="/">Erro. Tente Novamente.</a>'
    


@app.route("/comentarios", methods=["GET"])
def pag_main():

    comentarios = Comment.get_comentarios()

    return render_template("main.html", comentarios = comentarios)


@app.route("/post/comentarios", methods=["POST"])
def post_mensagem():
    # capturando as informações do usuario
    nome_user = request.form.get("input_user")
    comentario = request.form.get("input_message")
    
    if (Comment.create(nome_user, comentario)):

        # Redirecionando de volta

        Comment.get_comentarios()

        return redirect('/comentarios')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Comment.deletar_mensagem(codigo)
    return redirect("/")

@app.route("/put/curtida/mensagem/<codigo>")
def curtir_mensagem(codigo):
    Comment.curtir_mensagem(codigo)
    return redirect("/")

app.run(debug=True, host='0.0.0.0', port=8080)