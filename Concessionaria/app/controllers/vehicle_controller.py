from flask import request, render_template, redirect, url_for
from app.database.connection import getDatabaseConnection
from app.models.vehicle import Vehicle

# Função para registrar um novo veículo
def vehicle_register():
    error = None
    message = None

    if request.method == 'POST':
        # Captura os dados do veículo do formulário
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
        disponibilityVehicle = "Disponível"

        # Inserir os dados coletados no banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor()

        # Cria uma instância do veículo com os dados capturados
        vehicle = Vehicle(brandVehicle, modelVehicle, engineVehicle, plateVehicle, colorVehicle, yearVehicle, yearModel,
                          kmsVehicle, typeVehicle, conditionVehicle, chassiVehicle, renavamVehicle, buypriceVehicle, sellpriceVehicle, disponibilityVehicle)
        try:
            # Salva o veículo no banco de dados
            vehicle.save_to_db(cursor)
            conn.commit()
            message = f"Veículo cadastrado com sucesso!"
        except Exception as e:
            # Em caso de erro, faz rollback e define a mensagem de erro
            conn.rollback()
            error = f"Erro ao cadastrar veículo: {str(e)}"
        finally:
            # Fecha o cursor e a conexão com o banco de dados
            cursor.close()
            conn.close()

    # Renderiza o template de registro de veículo com as mensagens de erro ou sucesso
    return render_template('vehicle/register.html', username=request.cookies.get('username'), error=error, message=message)

# Função para buscar um veículo
def vehicle_search():
    vehicle_data = None
    error = None
    message = request.args.get('message')

    if request.method == 'POST':
        # Captura a placa do veículo do formulário
        plate = request.form['plate_vehicle']

        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Busca o veículo no banco de dados pela placa
            vehicle_data = Vehicle.find_by_plate(cursor, plate)
            if vehicle_data is None:
                error = "Veículo não encontrado"
        except Exception as e:
            # Em caso de erro, define a mensagem de erro
            error = f"Erro ao buscar veículo: {str(e)}"
        finally:
            # Fecha o cursor e a conexão com o banco de dados
            cursor.close()
            conn.close()

    # Renderiza o template de busca de veículo com os dados do veículo e mensagens de erro ou sucesso
    return render_template('vehicle/search.html', vehicle=vehicle_data, error=error, message=message, username=request.cookies.get('username'))

# Função para deletar um veículo
def delete_vehicle(plate):
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    try:
        # Deleta o veículo do banco de dados pela placa
        Vehicle.delete_by_plate(cursor, plate)
        conn.commit()
        message = "Veículo deletado com sucesso!"
    except Exception as e:
        # Em caso de erro, faz rollback e define a mensagem de erro
        conn.rollback()
        message = f"Erro ao deletar veículo: {e}"
    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()

    # Redireciona para a página de busca de veículo com a mensagem de sucesso ou erro
    return redirect(url_for('vehicle.vehicle_search', message=message))

# Função para editar um veículo
def edit_vehicle(plate):
    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    vehicle_data = None
    error = None
    message = None

    if request.method == 'GET':
        try:
            # Busca os dados do veículo no banco de dados pela placa
            vehicle_data = Vehicle.find_by_plate(cursor, plate)
            if not vehicle_data:
                error = "Veículo não encontrado"
        except Exception as e:
            # Em caso de erro, define a mensagem de erro
            error = f"Erro ao buscar veículo: {str(e)}"
        finally:
            # Fecha o cursor e a conexão com o banco de dados
            cursor.close()
            conn.close()

        # Renderiza o template de edição de veículo com os dados do veículo e mensagens de erro ou sucesso
        return render_template('vehicle/edit.html', vehicle=vehicle_data, error=error, message=message, username=request.cookies.get('username'))

    elif request.method == 'POST':
        # Captura os dados atualizados do veículo do formulário
        brandVehicle = request.form['brand_vehicle']
        modelVehicle = request.form['model_vehicle']
        engineVehicle = request.form['engine_vehicle']
        # plateVehicle = request.form['plate_vehicle']
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

        try:
            # Atualiza os dados do veículo no banco de dados
            Vehicle.update_by_plate(cursor, plate, brandVehicle, modelVehicle, engineVehicle, colorVehicle, yearVehicle, yearModel,
                                    kmsVehicle, typeVehicle, conditionVehicle, chassiVehicle, renavamVehicle, buypriceVehicle, sellpriceVehicle)
            conn.commit()
            message = "Veículo atualizado com sucesso"
        except Exception as e:
            # Em caso de erro, define a mensagem de erro
            error = f"Erro ao atualizar veículo: {str(e)}"
        finally:
            # Fecha o cursor e a conexão com o banco de dados
            cursor.close()
            conn.close()

        # Redireciona para a página de busca de veículo com a mensagem de sucesso ou erro
        return redirect(url_for('vehicle.vehicle_search', message=message))