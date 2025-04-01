from data.connection_controller import Connection

class User:

    def cadastrar_user(login, senha, nome):
        try:
            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute("INSERT INTO tb_usuarios (nome, login, senha) VALUES (%s, %s, %s);", (login, senha, nome))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True
        
        except:
            
            return False