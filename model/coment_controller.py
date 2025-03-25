from data.connection_controller import Connection
from datetime import datetime

class Comment:

    def create(name, comentario):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute("INSERT INTO tb_comentarios (nome, data_hora, comentario) VALUES (%s, %s, %s);", (name, datetime.now(), comentario))

            # Confirma a alteração

            conexao_db.commit()

            # Fecha a conexão com o Banco de Dados e o cursor

            cursor.close()
            conexao_db.close()

            return True

        except:

            return False
        
    def get_comentarios():

        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor(dictionary=True)

            cursor.execute('SELECT cod_comentario, nome, data_hora, comentario FROM tb_comentarios')

            comentarios_lista = cursor.fetchall()

            cursor.close()
            conexao_db.close()

            return comentarios_lista

        except:

            return []
    
    def deletar_mensagem(codigo):
        try:
            conexao_db = Connection.create()

            cursor = conexao_db.cursor()
            # pelo fato de ser uma tupla precisamos de 2 valores porem só por uma virgula para dar certo
            cursor.execute('DELETE FROM tb_comentarios WHERE cod_comentario = %s;', (codigo,))

            conexao_db.commit()

            cursor.close()

            conexao_db.close()
        except:
            return False

    def curtir_mensagem(codigo):
        try:
            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute('UPDATE tb_comentarios SET curtidas = curtidas + 1 WHERE cod_comentario = %s;', (codigo,))

            conexao_db.commit()

            cursor.close()

            conexao_db.close()
        except:
            return False
        
    def descurtir_mensagem(codigo):
        try:
            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute('UPDATE tb_comentarios SET curtidas = curtidas -1 WHERE cod_comentario = %s;', (codigo,))

            conexao_db.commit()

            cursor.close()

            conexao_db.close()
        except:
            return False
        