from flask import Flask, render_template, request
from database import getDatabaseConnection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
             placa, 
             chassi, 
             renavam, 
             km_rodado, 
             valor_compra, 
             valor_venda,
             condicao,
             categoria,          
            )

            VALUES (
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s,
                %s
            )
        """
        
        values = (brandVehicle, modelVehicle, yearVehicle, yearModel, colorVehicle, plateVehicle, chassiVehicle, renavamVehicle, kmsVehicle, buypriceVehicle, sellpriceVehicle, conditionVehicle,typeVehicle)

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

        return render_template('vehicle_register.html')
    return render_template('vehicle_register.html')

@app.route('/customer_register',  methods=['GET', 'POST'])
def customer_register():
    if request.method == "POST":
        # Captura os dados do cliente
        customerName = request.form['customer_name']
        customerCpf = request.form['customer_cpf']
        customerRg = request.form['customer_rg']
        customerBirthDate = request.form['customer_birth']
        customerSex = request.form['customer_sex']
        customerPhone = request.form['customer_phone']
        customerEmail = request.form['customer_email']
        customerAddress = request.form['customer_address']
        customerZipCode = request.form['customer_zip']
        customerCity = request.form['customer_city']
        customerState = request.form['customer_state']
        customerCountry = request.form['customer_country']

        # Conecta ao banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor()

        # Insere os dados do cliente no banco de dados
        cursor.execute(
            "INSERT INTO tb_clientes (nome_cliente, cpf_cliente, rg_cliente, data_nascimento, sexo_cliente, telefone_cliente, email_cliente, endereco_cliente, cep_cliente, cidade_cliente, estado_cliente, pais_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (customerName, customerCpf, customerRg, customerBirthDate, customerSex, customerPhone, customerEmail, customerAddress, customerZipCode, customerCity, customerState, customerCountry)
        )

        # Salva as alterações
        conn.commit()

        # Fecha a conexão
        cursor.close()
        conn.close()
    return render_template('customer_register.html')

@app.route('/employee_register')
def employee_register():
    return render_template('employee_register.html')

@app.route('/vehicle_search')
def vehicle_search():
    return render_template('vehicle_search.html')

@app.route('/customer_search')
def customer_search():
    return render_template('customer_search.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/sales_reports')
def sales_reports():
    return render_template('sales_reports.html')

@app.route('/stock_reports')
def stock_reports():
    return render_template('stock_reports.html')

if __name__ == '__main__':
    app.run(debug=True)