import mysql.connector

class Connection:

    def create():
        if True:    
            return mysql.connector.connect( 

                host='10.110.134.2', 
                port=3306, 
                user='3ds', 
                password='banana', 
                database='db_feedback'

            )
        else:
            return mysql.connector.connect(

                host='localhost',
                port=3306,
                user='root',
                password='root'
                database='db_feedback'
            )