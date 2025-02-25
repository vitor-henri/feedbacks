from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector

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

    #criando a conexao
    conexao = mysql.connector.connect(
        hostname = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "db_feedbacks")
    
    # criando o cursor ou seja o cara que vai do python ate o banco de dados como se fosse uma ponte
    cursor = conexao.cursor()

    # criando o comando SQL que sera executado no SQL
    sql = """INSERT INTO tb_feedback
        (name_user, comentario, data_comentario)
    VALUES
        (%s, %s, %s)"""
    
    # os %s sao os dados que serao informados no SQl como se fosse uma variavel entao usamos uma lista para guardar os dados 
    valores = [nome_user, comentario, data_comentario]

    # executando o comando SQL com o cursor
    cursor.execute(sql, valores)

    # confirmando a alteração no MYSQL como se fossse um comit do github
    conexao.commit()

    # fechando a conexao e o cursor
    cursor.close()
    conexao.close()

    return redirect("/")

app.run(debug=True)
