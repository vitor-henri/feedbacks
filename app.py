from flask import Flask, render_template, request, redirect
from model.coment_controller import Comment


app = Flask(__name__)

comentarios = []

# criando a rota para a pagina principal
@app.route("/", methods=["GET"])
def pag_main():

    comentarios = Comment.get_comentarios()

    return render_template("index.html", comentarios = comentarios)

@app.route("/post/comentarios", methods=["POST"])
def post_mensagem():
    # capturando as informações do usuario
    nome_user = request.form.get("input_user")
    comentario = request.form.get("input_comentario")
    
    if (Comment.create(nome_user, comentario)):

        # Redirecionando de volta

        Comment.get_comentarios()

        return redirect('/')
    
    else:

        return '<a href="/">Erro. Tente Novamente.</a>'

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Comment.deletar_mensagem(codigo)
    return redirect("/")


app.run(debug=True, host='0.0.0.0', port=8080)