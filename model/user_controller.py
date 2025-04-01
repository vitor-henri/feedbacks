from data.connection_controller import Connection
from hashlib import sha256

class User:

    def cadastrar_user(login, senha, nome):
        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute("INSERT INTO tb_usuarios (nome, login, senha) VALUES (%s, %s, %s);", (login, sha256(senha.encode().hexdigest()), nome))

            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            return True
        
        except:
            
            return False
    def logando_user(login,senha):
        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()

            cursor.execute("SELECT * FROM tb_usuarios WHERE login = %s AND bynary senha = %s;", (login, sha256(senha.encode().hexdigest())))

            resultado = cursor.fetchone()

            if(resultado == True):
                



