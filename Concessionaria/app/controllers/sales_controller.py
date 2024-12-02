from flask import request, render_template, redirect, url_for, flash
from app.database.connection import getDatabaseConnection

def sales():
    error = None
    message = None
    vehicleSaleSelector = []

    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT id_veiculo, marca, modelo, valor_venda, placa, disponibilidade FROM tb_veiculos WHERE disponibilidade = 'Disponível'")
        # Obtém os veículos disponíveis para mostrar na página de vendas
        vehicleSaleSelector = cursor.fetchall()

    except Exception as e:
        error = f"Erro ao buscar veículos: {str(e)}"
    finally:
        cursor.close()
        conn.close()

    if not vehicleSaleSelector:
        message = "Nenhum veículo disponível no momento."

    if request.method == "POST":
        vehicle_id = request.form.get('vehicle')

        conn = getDatabaseConnection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE tb_veiculos SET disponibilidade = 'Vendido' WHERE id_veiculo = %s", (vehicle_id,))
            conn.commit()
            flash("Venda registrada com sucesso", "success")
        except Exception as e:
            conn.rollback()
            error = f"Erro ao registrar venda: {str(e)}"
            flash(error, "error")
        finally:
            cursor.close()
            conn.close()

    return render_template('sales.html', vehicleSaleSelector=vehicleSaleSelector, username=request.cookies.get('username'), error=error, message=message)

def sale_register():
    vehicle_id = request.form.get('id_veiculo')

    conn = getDatabaseConnection()
    cursor = conn.cursor()
    message = None
    error = None

    try:
        cursor.execute(
            "UPDATE tb_veiculos SET disponibilidade = 'Vendido' WHERE id_veiculo = %s", (vehicle_id,))
        conn.commit()
        flash("Venda registrada com sucesso", "success")
    except Exception as e:
        conn.rollback()
        flash(f"Erro ao registrar venda: {str(e)}", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('sales', message=message, error=error))

def remove_vehicle(id_veiculo):
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM tb_veiculos WHERE id_veiculo = %s", (id_veiculo,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        flash(f"Erro ao remover veículo: {str(e)}", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('sales'))