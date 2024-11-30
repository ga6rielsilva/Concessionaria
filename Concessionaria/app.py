from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
import base64
import io
from PIL import Image
from database import getDatabaseConnection
import random

app = Flask(__name__)


@app.before_request
def restrict_access():
    if request.endpoint not in ['login', 'static'] and not is_logged():
        return redirect(url_for('login'))


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


@app.route('/', methods=['GET', 'POST'])
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
            response = make_response(redirect(url_for('index')))
            response.set_cookie('login', login)
            response.set_cookie('password', password)
            response.set_cookie('username', user[1])
            return response
        else:
            return render_template('login.html', error='Login ou senha inválidos')

    return render_template('login.html')


@app.route('/logout')
def logout():
    # Remove os cookies de login e senha
    response = make_response(redirect(url_for('login')))
    response.set_cookie('login', '', expires=0)
    response.set_cookie('password', '', expires=0)
    response.set_cookie('username', '', expires=0)
    return response


@app.route('/home')
def index():
    return render_template('index.html', username=request.cookies.get('username'))


@app.route('/vehicle_register',  methods=['GET', 'POST'])
def vehicle_register():
    error = None
    message = None

    if request.method == 'POST':
        # Captura os dados do veículo
        brandVehicle = request.form['brand_vehicle']
        modelVehicle = request.form['model_vehicle']
        engineVehicle = request.form['engine_vehicle']
        plateVehicle = request.form['plate_vehicle']
        colorVehicle = request.form['color_vehicle']
        yearVehicle = request.form['year_fabrication']
        yearModel = request.form['year_model']
        kmsVehicle = request.form['kms_vehicle']
        typeVehicle = request.form['type_vehicle']
        conditionVehicle = request.form['condition_vehicle']
        chassiVehicle = request.form['chassi_vehicle']
        renavamVehicle = request.form['renavam_vehicle']
        buypriceVehicle = request.form['buyprice_vehicle']
        sellpriceVehicle = request.form['sellprice_vehicle']

        # Inserir os dados coletados no banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor()
        query = """
            INSERT INTO tb_veiculos (
             marca,
             modelo,
             ano_fabricacao,
             ano_modelo,
             cor,
             motor_veiculo,
             placa,
             chassi,
             renavam,
             km_rodado,
             valor_compra,
             valor_venda,
             condicao,
             categoria
            )

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (brandVehicle, modelVehicle, yearVehicle, yearModel, colorVehicle, engineVehicle, plateVehicle,
                  chassiVehicle, renavamVehicle, kmsVehicle, buypriceVehicle, sellpriceVehicle, conditionVehicle, typeVehicle)

        try:
            cursor.execute(query, values)
            conn.commit()
            message = f"Veículo cadastrado com sucesso!"
        except Exception as e:
            conn.rollback()
            error = f"Erro ao cadastrar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('vehicle_register.html', username=request.cookies.get('username'), error=error, message=message)


@app.route('/customer_register',  methods=['GET', 'POST'])
def customer_register():
    error = None
    message = None

    if request.method == "POST":
        # Captura os dados do cliente
        nameCustomer = request.form['customer_name']
        cpfCustomer = request.form['customer_cpf']
        rgCustomer = request.form['customer_rg']
        birthCustomer = request.form['customer_birth']
        customerSex = request.form['customer_sex']
        phoneCustomer = request.form['customer_phone']
        emailCustomer = request.form['customer_email']
        addressCustomer = request.form['customer_address']
        cityCustomer = request.form['customer_city']
        stateCustomer = request.form['customer_state']
        zipCustomer = request.form['customer_zip']
        countryCustomer = request.form['customer_country']

        # Inserir os dados coletados no banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor()
        query = """
            INSERT INTO tb_clientes (
                nome_cliente,
                cpf_cliente,
                rg_cliente,
                data_nascimento,
                sexo_cliente,
                telefone_cliente,
                email_cliente,
                endereco_cliente,
                cep_cliente,
                cidade_cliente,
                estado_cliente,
                pais_cliente
            )

            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (nameCustomer, cpfCustomer, rgCustomer, birthCustomer, customerSex, phoneCustomer,
                  emailCustomer, addressCustomer, zipCustomer, cityCustomer, stateCustomer, countryCustomer)

        try:
            cursor.execute(query, values)
            conn.commit()
            message = f"Cliente cadastrado com sucesso!"
        except Exception as e:
            conn.rollback()
            error = f"Erro ao cadastrar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('customer_register.html', username=request.cookies.get('username'), error=error, message=message)


@app.route('/employee_register', methods=['GET', 'POST'])
def employee_register():
    message = None
    error = None

    if request.method == "POST":
        
        photo_file = request.files['profilePhoto']
        img_data = photo_file.read()

        try:
            image = Image.open(io.BytesIO(img_data))
            img_type = image.format.lower()
            if img_type != "png":
                img_converted = io.BytesIO()
                image.save(img_converted, format="PNG")
                img_data = img_converted.getvalue()
                img_type = "png"
        except Exception as e:
            error = f"Erro ao processar a imagem: {e}"
            img_data = None
            img_type = None
            

        nameEmployee = request.form['employee_name']
        cpfEmployee = request.form['employee_cpf']
        rgEmployee = request.form['employee_rg']
        birthEmployee = request.form['employee_birth']
        sexEmployee = request.form['employee_sex']
        employeePosition = request.form['employee_position']
        emailEmployee = request.form['employee_email']
        phoneEmployee = request.form['employee_phone']
        addressEmployee = request.form['employee_address']
        cityEmployee = request.form['employee_city']
        stateEmployee = request.form['employee_state']
        zipEmployee = request.form['employee_zip']
        countryEmployee = request.form['employee_country']

        # Gerar login padrão
        name_parts = nameEmployee.split()
        if len(name_parts) >= 2:
            base_login = f"{name_parts[0].lower()}_{name_parts[-1].lower()}"
        else:
            base_login = name_parts[0].lower()

        # Conexão com o banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor()

        # Garantir que o login seja único
        userLogin = base_login
        counter = 1
        while True:
            cursor.execute(
                "SELECT COUNT(*) FROM tb_usuarios WHERE login = %s", (userLogin,))
            if cursor.fetchone()[0] == 0:
                break  # Login é único
            userLogin = f"{base_login}{counter}"  # Incrementar contador
            counter += 1

        # Gerar senha aleatória de 6 dígitos
        userPassword = str(random.randint(100000, 999999))

        try:
            # Inserir o usuário na tabela tb_usuarios
            user_query = """
                INSERT INTO tb_usuarios (
                    nome,
                    login,
                    senha
                )
                VALUES (%s, %s, %s)
            """
            user_values = (nameEmployee, userLogin, userPassword)
            cursor.execute(user_query, user_values)

            # Recuperar o ID do usuário recém-criado
            userId = cursor.lastrowid

            # Inserir o funcionário na tabela tb_funcionarios
            employee_query = """
                INSERT INTO tb_funcionarios (
                    foto_funcionario,
                    nome_funcionario,
                    cpf_funcionario,
                    rg_funcionario,
                    data_nascimento,
                    sexo_funcionario,
                    cargo_funcionario,
                    email_funcionario,
                    telefone_funcionario,
                    endereco_funcionario,
                    cidade_funcionario,
                    estado_funcionario,
                    cep_funcionario,
                    pais_funcionario,
                    id_usuario
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            employee_values = (
                img_data, nameEmployee, cpfEmployee, rgEmployee, birthEmployee,
                sexEmployee, employeePosition, emailEmployee, phoneEmployee,
                addressEmployee, cityEmployee, stateEmployee, zipEmployee,
                countryEmployee, userId
            )
            cursor.execute(employee_query, employee_values)

            # Confirmar a transação
            conn.commit()
            message = f"Funcionário e usuário cadastrados com sucesso!<br> Login: {

                userLogin}<br> Senha: {userPassword}"
        except Exception as e:
            conn.rollback()
            error = f"Erro ao cadastrar funcionário e usuário: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('employee_register.html',  username=request.cookies.get('username'), message=message, error=error)


@app.route('/vehicle_search', methods=['GET', 'POST'])
def vehicle_search():
    vehicle_data = None
    error = None
    message = request.args.get('message')

    if request.method == 'POST':
        plate = request.form['plate_vehicle']

        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT * FROM tb_veiculos
                WHERE placa = %s
            """

        value = (plate,)

        try:
            cursor.execute(query, value)
            vehicle_data = cursor.fetchone()
            if vehicle_data is None:
                error = "Veículo não encontrado"
        except Exception as e:
            error = f"Erro ao buscar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('vehicle_search.html', vehicle=vehicle_data, error=error, message=message, username=request.cookies.get('username'))


@app.route('/delete-vehicle/<string:plate>', methods=['POST'])
def delete_vehicle(plate):
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    query = """
        DELETE FROM tb_veiculos
        WHERE placa = %s
    """
    value = (plate,)

    try:
        cursor.execute(query, value)
        conn.commit()
        message = "Veículo excluído com sucesso"
    except Exception as e:
        message = f"Erro ao excluir veículo: {str(e)}"
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('vehicle_search', message=message))


@app.route('/customer_search', methods=['GET', 'POST'])
def customer_search():
    customer_data = None
    error = None
    if request.method == 'POST':
        cpf = request.form['cpf_customer']

        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT * FROM tb_clientes
                WHERE cpf_cliente = %s
            """

        value = (cpf,)

        try:
            cursor.execute(query, value)
            customer_data = cursor.fetchone()
            if customer_data is None:
                error = "Cliente não encontrado"
        except Exception as e:
            error = f"Erro ao buscar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('customer_search.html', username=request.cookies.get('username'), customers=customer_data, error=error)


@app.route('/reports')
def reports():
    return render_template('reports.html', username=request.cookies.get('username'))


@app.route('/sales', methods=['GET', 'POST'])
def sales():
    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    vehicleSaleSelector = []
    message = None
    error = None

    try:
        cursor.execute(
            "SELECT id_veiculo, marca, modelo, valor_venda, placa FROM tb_veiculos")
        vehicleSaleSelector = cursor.fetchall()  # Obtém todos os veículos

    except Exception as e:
        error = f"Erro ao buscar veículos: {str(e)}"
    finally:
        cursor.close()
        conn.close()

    if not vehicleSaleSelector:
        message = "Nenhum veículo disponível no momento."

    return render_template(
        'sales.html',
        # Passando todos os veículos para o template
        vehicleSaleSelector=vehicleSaleSelector,
        username=request.cookies.get('username'),
        message=message,
        error=error
    )


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    error = None
    message = None
    img_base64 = None

    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            error = "As senhas não coincidem"
        else:
            conn = getDatabaseConnection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT senha FROM tb_usuarios WHERE nome = %s", (request.cookies.get(
                    'username'),)
            )
            current_password_db = cursor.fetchone()
            if current_password_db:
                current_password_db = current_password_db['senha']
            else:
                error = "Usuário não encontrado"
            if current_password_db != current_password:
                error = "Senha atual incorreta"
            else:
                cursor.execute(
                    "UPDATE tb_usuarios SET senha = %s WHERE nome = %s", (
                        new_password, request.cookies.get('username'))
                )
                conn.commit()
                message = "Senha atualizada com sucesso"
    
    login = request.cookies.get('login')
    
    if login:
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
            print("foto selecionada")
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
                    img_base64 = f"data:image/{img_type};base64," + base64.b64encode(img_data).decode('utf-8')
                else:
                    img_base64 = None
            else:
                img_base64 = None
    
    # Processamento da foto
    if 'profilePhoto' in request.files:
        profilePhoto = request.files['profilePhoto']
        if profilePhoto:
            img_data = profilePhoto.read()
            img_type = profilePhoto.content_type.split('/')[-1]
            if img_type != "png":
                img_converted = io.BytesIO()
                image = Image.open(io.BytesIO(img_data))
                image.save(img_converted, format="PNG")
                img_data = img_converted.getvalue()
                img_type = "png"

            conn = getDatabaseConnection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tb_funcionarios
                SET foto_funcionario = %s
                WHERE id_usuario = %s
            """, (img_data, id_user))
            conn.commit()
            message = "Foto de perfil atualizada com sucesso"
            cursor.close()
            conn.close()

            return jsonify({'success': True})


    return render_template('settings.html', error=error, message=message, username=request.cookies.get('username'), img_base64=img_base64)


if __name__ == '__main__':

    try:
        conn = getDatabaseConnection()
        conn.close()
    finally:
        app.run(debug=True)
