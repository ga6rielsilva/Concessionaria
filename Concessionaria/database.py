import mysql.connector

def getDatabaseConnection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='erp_concessionaria'
    )
    return conn
