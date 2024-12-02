import mysql.connector
from mysql.connector import errorcode

def execute_sql_file(cursor, sql_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as file:
        sql_commands = file.read().split(';')  # Divide os comandos pelo delimitador ";"
        for command in sql_commands:
            if command.strip():  # Ignora comandos vazios
                try:
                    cursor.execute(command)
                except mysql.connector.Error as err:
                    print(f"Erro ao executar o comando: {command}\nErro: {err}")

def getDatabaseConnection():
    try:
        # Tenta se conectar ao banco de dados específico
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='concessionaria'
        )
        return conn
    except mysql.connector.Error as err:
        # Verifica se o erro foi causado pela ausência do banco de dados
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados 'concessionaria' não encontrado. Criando banco a partir do arquivo SQL...")
            # Conecta ao MySQL sem selecionar um banco de dados
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=''
            )
            cursor = conn.cursor()
            # Executa o script SQL para criar o banco e tabelas
            execute_sql_file(cursor, 'banco_de_dados/concessionaria.sql')
            print("Banco de dados e tabelas criados com sucesso!")
            conn.database = 'concessionaria'  # Redefine o banco para o objeto de conexão
            return conn
        else:
            print(f"Erro ao conectar ao banco de dados: {err}")
            raise
