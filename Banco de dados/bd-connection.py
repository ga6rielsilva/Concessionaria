import mysql.connector

# Estabelecer conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='erp_concessionaria'
)

# Criar um cursor para manipular o banco de dados
cursor = conn.cursor()