from data.connection_controller import Connection
from hashlib import sha256

class User:

    def cadastrar_user(nome, login, senha):
        try:

            conexao_db = Connection.create()

            cursor = conexao_db.cursor()
            
            senha = sha256(senha.encode()).hexdigest()

            cursor.execute("INSERT INTO tb_usuarios (nome, login, senha) VALUES (%s, %s, %s);", (nome, login, senha))

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

            senha = sha256(senha.encode()).hexdigest()
            
            cursor.execute("SELECT * FROM tb_usuarios WHERE login = %s AND binary senha = %s;", (login, senha))

            resultado = cursor.fetchone()

            cursor.close()
            conexao_db.close()
            
            if(resultado == True):
               return True 
           
        except:
            
            return False



