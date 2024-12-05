from flask import render_template, request
from app.database.connection import getDatabaseConnection
import base64
import io
from PIL import Image

def settings():
    error = None
    message = None
    img_base64 = None

    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Obtém as senhas do formulário
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Verifica se todas as senhas foram fornecidas
        if current_password and new_password and confirm_password:
            # Verifica se as novas senhas coincidem
            if new_password != confirm_password:
                error = "As senhas não coincidem"
            else:
                # Conecta ao banco de dados
                conn = getDatabaseConnection()
                cursor = conn.cursor(dictionary=True)
                # Busca a senha atual do usuário no banco de dados
                cursor.execute(
                    "SELECT senha FROM tb_usuarios WHERE nome = %s", (request.cookies.get('username'),)
                )
                current_password_db = cursor.fetchone()
                cursor.fetchall()

                # Verifica se o usuário foi encontrado
                if current_password_db:
                    current_password_db = current_password_db['senha']
                else:
                    error = "Usuário não encontrado"
                # Verifica se a senha atual está correta
                if current_password_db != current_password:
                    error = "Senha atual incorreta"
                else:
                    # Atualiza a senha no banco de dados
                    cursor.execute(
                        "UPDATE tb_usuarios SET senha = %s WHERE nome = %s", (
                            new_password, request.cookies.get('username'))
                    )
                    conn.commit()
                    message = "Senha atualizada com sucesso"

    # Obtém o login do cookie
    login = request.cookies.get('login')

    if login:
        # Conecta ao banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)

        # Obter ID do usuário
        query = """
            SELECT id_usuario FROM tb_usuarios
            WHERE login = %s
        """
        cursor.execute(query, (login,))
        user = cursor.fetchone()

        if user:
            id_user = user['id_usuario']

            # Obter a foto do funcionário (campo BLOB)
            query = """
                SELECT foto_funcionario FROM tb_funcionarios
                WHERE id_usuario = %s
            """
            cursor.execute(query, (id_user,))
            photo = cursor.fetchone()
            if photo and photo['foto_funcionario']:
                # Converte o conteúdo binário da foto para base64
                img_data = photo['foto_funcionario']

                # Detectar o formato da imagem com Pillow
                img_type = None
                try:
                    image = Image.open(io.BytesIO(img_data))
                    img_type = image.format.lower()  # Formato da imagem (jpeg, png, etc.)
                except Exception as e:
                    print(f"Erro ao detectar o tipo de imagem: {e}")

                if img_type:
                    # Converte a imagem para base64
                    img_base64 = f"data:image/{img_type};base64," + \
                        base64.b64encode(img_data).decode('utf-8')
                else:
                    img_base64 = None
            else:
                img_base64 = None

    # Processamento da foto
    if request.method == 'POST':
        profilePhoto = request.files['profilePhoto']
        if profilePhoto:
            # Lê os dados da foto
            img_data = profilePhoto.read()
            img_type = profilePhoto.content_type.split('/')[-1]
            # Converte a imagem para PNG se necessário
            if img_type != "png":
                img_converted = io.BytesIO()
                image = Image.open(io.BytesIO(img_data))
                image.save(img_converted, format="PNG")
                img_data = img_converted.getvalue()
                img_type = "png"

            # Atualiza a foto do funcionário no banco de dados
            conn = getDatabaseConnection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tb_funcionarios
                SET foto_funcionario = %s
                WHERE id_usuario = %s
            """, (img_data, id_user))
            message = "Foto atualizada com sucesso"
            conn.commit()
            cursor.close()
            conn.close()

    # Renderiza o template settings.html com as variáveis de contexto
    return render_template('settings.html', error=error, message=message, username=request.cookies.get('username'), img_base64=img_base64)