from data.connection_controller import Connection

class Comment:

    def create(name, comentario):

        try:

            conexao_db = Connection.create()

            # O cursor é responsável por manipular o Banco de Dados

            cursor = conexao_db.cursor()

            cursor.execute("INSERT INTO tb_feedback (name_user, comentario) VALUES (%s, %s);", (name, comentario))

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

            cursor.execute('SELECT name_user, comentario, data_comentario FROM tb_feedback')

            comentarios_lista = cursor.fetchall()

            cursor.close()
            conexao_db.close()

            return comentarios_lista

        except:

            return []