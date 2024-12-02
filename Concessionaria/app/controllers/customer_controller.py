from flask import request, render_template, redirect, url_for
from app.database.connection import getDatabaseConnection
from app.models.customer import Customer

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

        customer = Customer(nameCustomer, cpfCustomer, rgCustomer, birthCustomer, customerSex, phoneCustomer,
                            emailCustomer, addressCustomer, zipCustomer, cityCustomer, stateCustomer, countryCustomer)
        try:
            customer.save_to_db(cursor)
            conn.commit()
            message = f"Cliente cadastrado com sucesso!"
        except Exception as e:
            conn.rollback()
            error = f"Erro ao cadastrar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('customer/register.html', username=request.cookies.get('username'), error=error, message=message)

def customer_search():
    customer_data = None
    error = None
    message = request.args.get('message')

    if request.method == 'POST':
        cpf = request.form['cpf_customer']

        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)

        try:
            customer_data = Customer.find_by_cpf(cursor, cpf)
            if customer_data is None:
                error = "Cliente não encontrado"
        except Exception as e:
            error = f"Erro ao buscar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('customer/search.html', username=request.cookies.get('username'), customer=customer_data, error=error, message=message)

def delete_customer(cpf):
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    try:
        Customer.delete_by_cpf(cursor, cpf)
        conn.commit()
        message = "Cliente deletado com sucesso!"
        print(message)
    except Exception as e:
        conn.rollback()
        message = f"Erro ao deletar cliente: {e}"
        print(message)
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('customer.customer_search', message=message))

def edit_customer(cpf):
    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    customer_data = None
    error = None
    message = None

    if request.method == 'GET':
        try:
            customer_data = Customer.find_by_cpf(cursor, cpf)
            if not customer_data:
                error = "Cliente não encontrado"
        except Exception as e:
            error = f"Erro ao buscar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

        return render_template('customer/edit.html', customer=customer_data, error=error, message=message, username=request.cookies.get('username'))

    elif request.method == 'POST':
        nameCustomer = request.form['customer_name']
        rgCustomer = request.form['customer_rg']
        birthCustomer = request.form['customer_birth']
        customerSex = request.form['customer_sex']
        phoneCustomer = request.form['customer_phone']
        emailCustomer = request.form['customer_email']
        addressCustomer = request.form['customer_address']
        stateCustomer = request.form['customer_state']
        zipCustomer = request.form['customer_zip']
        cityCustomer = request.form['customer_city']
        countryCustomer = request.form['customer_country']

        try:
            Customer.update_by_cpf(cursor, cpf, nameCustomer, rgCustomer, birthCustomer, customerSex, phoneCustomer,
                                   emailCustomer, addressCustomer, zipCustomer, cityCustomer, stateCustomer, countryCustomer)
            conn.commit()
            message = "Cliente atualizado com sucesso"
        except Exception as e:
            error = f"Erro ao atualizar cliente: {str(e)}"
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('customer.customer_search', message=message))