from flask import request, render_template, redirect, url_for, flash
from app.database.connection import getDatabaseConnection

# Função para exibir a página de vendas e registrar uma venda
def sales():
    error = None
    message = None
    vehicleSaleSelector = []

    # Conecta ao banco de dados
    conn = getDatabaseConnection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Seleciona os veículos disponíveis para venda
        cursor.execute(
            "SELECT id_veiculo, marca, modelo, valor_venda, placa, disponibilidade FROM tb_veiculos WHERE disponibilidade = 'Disponível'")
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

        # Conecta ao banco de dados para registrar a venda
        conn = getDatabaseConnection()
        cursor = conn.cursor()

        try:
            # Atualiza o status do veículo para 'Vendido'
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

    # Renderiza a página de vendas com os veículos disponíveis
    return render_template('sales.html', vehicleSaleSelector=vehicleSaleSelector, username=request.cookies.get('username'), error=error, message=message)

# Função para registrar a venda de um veículo
def sale_register():
    vehicle_id = request.form.get('id_veiculo')

    # Conecta ao banco de dados
    conn = getDatabaseConnection()
    cursor = conn.cursor()
    message = None
    error = None

    try:
        # Atualiza o status do veículo para 'Vendido'
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

    # Redireciona para a página de vendas
    return redirect(url_for('sales', message=message, error=error))

# Função para remover um veículo do banco de dados
def remove_vehicle(id_veiculo):
    # Conecta ao banco de dados
    conn = getDatabaseConnection()
    cursor = conn.cursor()

    try:
        # Remove o veículo do banco de dados
        cursor.execute(
            "DELETE FROM tb_veiculos WHERE id_veiculo = %s", (id_veiculo,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        flash(f"Erro ao remover veículo: {str(e)}", "error")
    finally:
        cursor.close()
        conn.close()

    # Redireciona para a página de vendas
    return redirect(url_for('sales'))