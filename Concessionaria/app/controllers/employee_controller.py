from flask import request, render_template, redirect, url_for
from app.database.connection import getDatabaseConnection
from app.models.employee import Employee
import random
import io
from PIL import Image

def employee_register():
    error = None
    message = None

    if request.method == "POST":
        # Captura os dados do funcionário
        nameEmployee = request.form['employee_name']
        cpfEmployee = request.form['employee_cpf']
        rgEmployee = request.form['employee_rg']
        birthEmployee = request.form['employee_birth']
        employeeSex = request.form['employee_sex']
        phoneEmployee = request.form['employee_phone']
        emailEmployee = request.form['employee_email']
        addressEmployee = request.form['employee_address']
        cityEmployee = request.form['employee_city']
        stateEmployee = request.form['employee_state']
        zipEmployee = request.form['employee_zip']
        countryEmployee = request.form['employee_country']
        employeePosition = request.form['employee_position']

        photo_file = request.files.get('profilePhoto')
        img_data = None

        if photo_file and photo_file.filename:
            try:
                img_data = photo_file.read()
                image = Image.open(io.BytesIO(img_data))
                img_type = image.format.lower()

                if img_type != "png":
                    img_converted = io.BytesIO()
                    image.save(img_converted, format="PNG")
                    img_data = img_converted.getvalue()
            except Exception as e:
                error = f"Erro ao processar a imagem: {e}"
                img_data = None

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
                employeeSex, employeePosition, emailEmployee, phoneEmployee,
                addressEmployee, cityEmployee, stateEmployee, zipEmployee,
                countryEmployee, userId
            )
            cursor.execute(employee_query, employee_values)

            # Confirmar a transação
            conn.commit()
            message = f"Funcionário e usuário cadastrados com sucesso!<br> Login: {userLogin}<br> Senha: {userPassword}"

        except Exception as e:
            conn.rollback()
            error = f"Erro ao cadastrar funcionário e usuário: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('employee/register.html', username=request.cookies.get('username'), error=error, message=message)

def employee_search():
    employee_data = None
    error = None
    message = request.args.get('message')

    if request.method == 'POST':
        cpf = request.form['cpf_employee']

        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)

        try:
            employee_data = Employee.find_by_cpf(cursor, cpf)
            if employee_data is None:
                error = "Funcionário não encontrado"
        except Exception as e:
            error = f"Erro ao buscar funcionário: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('employee/search.html', username=request.cookies.get('username'), employees=employee_data, error=error, message=message)

def delete_employee(cpf):
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    try:
        Employee.delete_by_cpf(cursor, cpf)
        conn.commit()
        message = "Funcionário deletado com sucesso!"
    except Exception as e:
        conn.rollback()
        message = f"Erro ao deletar funcionário: {e}"
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('employee/search', message=message))

def edit_employee(cpf):
    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    employee_data = None
    error = None
    message = None

    if request.method == 'GET':
        try:
            employee_data = Employee.find_by_cpf(cursor, cpf)
            if not employee_data:
                error = "Funcionário não encontrado"
        except Exception as e:
            error = f"Erro ao buscar funcionário: {str(e)}"
        finally:
            cursor.close()
            conn.close()

        return render_template('employee/edit.html', employee=employee_data, error=error, message=message, username=request.cookies.get('username'))

    elif request.method == 'POST':
        nameEmployee = request.form['employee_name']
        rgEmployee = request.form['employee_rg']
        birthEmployee = request.form['employee_birth']
        employeeSex = request.form['employee_sex']
        phoneEmployee = request.form['employee_phone']
        emailEmployee = request.form['employee_email']
        addressEmployee = request.form['employee_address']
        cityEmployee = request.form['employee_city']
        stateEmployee = request.form['employee_state']
        zipEmployee = request.form['employee_zip']
        countryEmployee = request.form['employee_country']

        try:
            Employee.update_by_cpf(cursor, cpf, nameEmployee, rgEmployee, birthEmployee, employeeSex, phoneEmployee,
                                   emailEmployee, addressEmployee, zipEmployee, cityEmployee, stateEmployee, countryEmployee)
            conn.commit()
            message = "Funcionário atualizado com sucesso"
        except Exception as e:
            error = f"Erro ao atualizar funcionário: {str(e)}"
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('employee/search', message=message))