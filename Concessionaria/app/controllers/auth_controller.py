from flask import request, redirect, url_for, make_response, render_template
from app.database.connection import getDatabaseConnection
import os
from PIL import Image
from io import BytesIO

# Função para restringir o acesso a determinados endpoints se o usuário não estiver logado
def restrict_access():
    allowed_endpoints = ['auth.login', 'static']
    if request.endpoint not in allowed_endpoints and not is_logged():
        return redirect(url_for('auth.login'))

# Função para verificar se o usuário está logado verificando os cookies
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

# Função para lidar com o login do usuário
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

# Função para criar usuário e funcionário padrão
def userEmployeeForAdmin():
    try:
        conn = getDatabaseConnection()
        cursor = conn.cursor()

        # Verificar se já existe algum administrador
        cursor.execute("SELECT id_usuario FROM tb_usuarios WHERE id_usuario = 1")
        user_exists = cursor.fetchone()

        if not user_exists:
            # Caso não exista ele cria um usuário administrador
            cursor.execute("""
                INSERT INTO tb_usuarios (id_usuario, nome, login, senha)
                VALUES (1, 'Frank', 'admin', 'admin')
            """)
            print("Usuário administrador criado com sucesso.")

        # Verificar se o funcionário associado já existe
        cursor.execute("SELECT id_funcionario FROM tb_funcionarios WHERE id_funcionario = 1")
        employee_exists = cursor.fetchone()

        if not employee_exists:
            # Caso não exista ele cria um funcionário para o usuário administrador
            employee_query = """
                INSERT INTO tb_funcionarios (id_funcionario, foto_funcionario, nome_funcionario, cpf_funcionario, rg_funcionario, id_usuario)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            # Utiliza o caminho absoluto da imagem de perfil padrão para o funcionário
            profileImgPath = os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'img', 'profile.png')
            )

            if os.path.exists(profileImgPath):
                with open(profileImgPath, "rb") as image_file:
                    img_data = image_file.read()

                    # Converte a imagem para PNG se necessário
                    img_converted = BytesIO()
                    image = Image.open(BytesIO(img_data))
                    image.save(img_converted, format="PNG")
                    img_data = img_converted.getvalue()

                    values = (1, img_data, 'Frank', '000.000.000-00', '00.000.000-0', 1)
                    cursor.execute(employee_query, values)
                    print("Funcionário administrador criado com sucesso.")
            else:
                print(f"Não foi possível encontrar a imagem para o perfil do funcionário administrador no caminho: {profileImgPath}")
        conn.commit()

    except Exception as e:
        print('Erro ao configurar usuário e funcionário administrador:', e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Função para lidar com o logout do usuário
def logout():
    response = make_response(redirect(url_for('auth.login')))
    response.set_cookie('login', '', expires=0)
    response.set_cookie('password', '', expires=0)
    response.set_cookie('username', '', expires=0)
    return response

# Função para renderizar a página inicial
def home():
    return render_template('index.html', username=request.cookies.get('username'))