from flask import Flask, render_template, request, redirect, url_for, make_response
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
            print("Veículo cadastrado com sucesso!")
        except Exception as e:
            conn.rollback()
            print("\n\nErro ao cadastrar veículo: " + str(e) + "\n\n")
        finally:
            cursor.close()
            conn.close()

    return render_template('vehicle_register.html', username=request.cookies.get('username'))


@app.route('/customer_register',  methods=['GET', 'POST'])
def customer_register():
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
            print("Cliente cadastrado com sucesso!")
        except Exception as e:
            conn.rollback()
            print("\n\nErro ao cadastrar cliente: " + str(e) + "\n\n")
        finally:
            cursor.close()
            conn.close()

    return render_template('customer_register.html', username=request.cookies.get('username'))


@app.route('/employee_register', methods=['GET', 'POST'])
def employee_register():
    message = None
    error = None

    if request.method == "POST":
        # Dados do funcionário
        photoEmployee = request.form['profilePhoto']
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
                photoEmployee, nameEmployee, cpfEmployee, rgEmployee, birthEmployee,
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

    return render_template('employee_register.html', username=request.cookies.get('username'), message=message, error=error)


@app.route('/vehicle_search', methods=['GET', 'POST'])
def vehicle_search():
    vehicle_data = None
    error = None
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
            print(vehicle_data)
            if vehicle_data is None:
                error = "Veículo não encontrado"
        except Exception as e:
            print(f"Erro ao buscar veículo: {str(e)}")
            error = f"Erro ao buscar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('vehicle_search.html', vehicle=vehicle_data, error=error, username=request.cookies.get('username'))


@app.route('/customer_search' , methods=['GET', 'POST'])
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
            print(customer_data)
            if customer_data is None:
                error = "Cliente não encontrado"
        except Exception as e:
            print(f"Erro ao buscar cliente: {str(e)}")
            error = f"Erro ao buscar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('customer_search.html', username=request.cookies.get('username'), customers=customer_data, error=error)


@app.route('/reports')
def reports():
    return render_template('reports.html', username=request.cookies.get('username'))


@app.route('/sale')
def sale():
    return render_template('sale.html', username=request.cookies.get('username'))


if __name__ == '__main__':

    try:
        conn = getDatabaseConnection()
        conn.close()
    finally:
        app.run(debug=True)
