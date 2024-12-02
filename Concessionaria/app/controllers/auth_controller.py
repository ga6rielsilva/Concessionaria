from flask import request, redirect, url_for, make_response, render_template
from app.database.connection import getDatabaseConnection

def restrict_access():
    if request.endpoint not in ['auth.login', 'static'] and not is_logged():
        return redirect(url_for('auth.login'))

def is_logged():
    login = request.cookies.get('login')
    password = request.cookies.get('password')
    if not login or not password:
        return False

    conn = getDatabaseConnection()
    cursor = conn.cursor()
    query = """
        SELECT * FROM tb_usuarios
        WHERE login = %s AND senha = %s
    """
    cursor.execute(query, (login, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        conn = getDatabaseConnection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM tb_usuarios
            WHERE login = %s AND senha = %s
        """
        cursor.execute(query, (login, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            response = make_response(redirect(url_for('index.home')))
            response.set_cookie('login', login)
            response.set_cookie('password', password)
            response.set_cookie('username', user[1])
            return response
        else:
            return render_template('login.html', error='Login ou senha inválidos')

    return render_template('login.html')

def logout():
    response = make_response(redirect(url_for('auth.login')))
    response.set_cookie('login', '', expires=0)
    response.set_cookie('password', '', expires=0)
    response.set_cookie('username', '', expires=0)
    return response

def home():
    return render_template('index.html', username=request.cookies.get('username'))