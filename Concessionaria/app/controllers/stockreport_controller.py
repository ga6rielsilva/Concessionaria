from flask import request, render_template, redirect, url_for
from app.database.connection import getDatabaseConnection

def stockreport():
    error = None
    message = None
    vehicles = []

    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute('SELECT * FROM tb_veiculos')
        vehicles = cursor.fetchall()
    except Exception as e:
        error = f"Erro ao buscar veículos: {str(e)}"
    finally:
        cursor.close()
        conn.close()

    if not vehicles:
        message = "Nenhum veículo disponível no momento."

    
    return render_template('stockreport.html', username=request.cookies.get('username'), error=error, message=message, vehicles=vehicles)
    
