# Dev by Vitor
from flask import Flask, render_template, request, redirect
from model.coment_controller import Comment
from model.user_controller import User


app = Flask(__name__)

app.secret_key = "vitor"

comentarios = []

# criando a rota para a pagina principal
@app.route("/")
def pag_login():
    return render_template("login.html")


@app.route("/cadastro", methods=["GET"])
def pag_cadastro():
    return render_template("cadastro.html")

@app.route("/post/cadastro", methods=["POST"])
def cadastro_usuario():
    
    nome = request.form.get("input__nome")
    login = request.form.get("input__user")    
    senha = request.form.get("input__senha")
    
    if(User.cadastrar_user(nome, login, senha)):

        return render_template("login.html", nome = nome, login = login, senha = senha)
    
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

@app.route("/login")
def pag_inicial():
    return render_template("main.html")

@app.route("/post/logar", methods=["POST"])
def post_logar():
    
    usuario = request.form.get("input__user")
    senha = request.form.get("input__senha")
    
    checker_logado = User.logando_user(usuario,senha)
    
    if checker_logado:
        return redirect("/comentarios")
    else:
        return redirect("/login")
    
if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=8080)