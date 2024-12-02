from flask import request, render_template, redirect, url_for
from app.database.connection import getDatabaseConnection
from app.models.vehicle import Vehicle

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
        disponibilityVehicle = "Disponível"

        # Inserir os dados coletados no banco de dados
        conn = getDatabaseConnection()
        cursor = conn.cursor()

        vehicle = Vehicle(brandVehicle, modelVehicle, engineVehicle, plateVehicle, colorVehicle, yearVehicle, yearModel,
                          kmsVehicle, typeVehicle, conditionVehicle, chassiVehicle, renavamVehicle, buypriceVehicle, sellpriceVehicle, disponibilityVehicle)
        try:
            vehicle.save_to_db(cursor)
            conn.commit()
            message = f"Veículo cadastrado com sucesso!"
        except Exception as e:
            conn.rollback()
            error = f"Erro ao cadastrar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('vehicle/register.html', username=request.cookies.get('username'), error=error, message=message)

def vehicle_search():
    vehicle_data = None
    error = None
    message = request.args.get('message')

    if request.method == 'POST':
        plate = request.form['plate_vehicle']

        conn = getDatabaseConnection()
        cursor = conn.cursor(dictionary=True)

        try:
            vehicle_data = Vehicle.find_by_plate(cursor, plate)
            if vehicle_data is None:
                error = "Veículo não encontrado"
        except Exception as e:
            error = f"Erro ao buscar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

    return render_template('vehicle/search.html', vehicle=vehicle_data, error=error, message=message, username=request.cookies.get('username'))

def delete_vehicle(plate):
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    try:
        Vehicle.delete_by_plate(cursor, plate)
        conn.commit()
        message = "Veículo deletado com sucesso!"
    except Exception as e:
        conn.rollback()
        message = f"Erro ao deletar veículo: {e}"
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('vehicle.vehicle_search', message=message))

def edit_vehicle(plate):
    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    vehicle_data = None
    error = None
    message = None

    if request.method == 'GET':
        try:
            vehicle_data = Vehicle.find_by_plate(cursor, plate)
            if not vehicle_data:
                error = "Veículo não encontrado"
        except Exception as e:
            error = f"Erro ao buscar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

        return render_template('vehicle/edit.html', vehicle=vehicle_data, error=error, message=message, username=request.cookies.get('username'))

    elif request.method == 'POST':
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

        try:
            Vehicle.update_by_plate(cursor, plate, brandVehicle, modelVehicle, engineVehicle, colorVehicle, yearVehicle, yearModel,
                                    kmsVehicle, typeVehicle, conditionVehicle, chassiVehicle, renavamVehicle, buypriceVehicle, sellpriceVehicle)
            conn.commit()
            message = "Veículo atualizado com sucesso"
        except Exception as e:
            error = f"Erro ao atualizar veículo: {str(e)}"
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('vehicle.vehicle_search', message=message))