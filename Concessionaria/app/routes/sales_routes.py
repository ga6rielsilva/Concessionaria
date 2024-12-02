from flask import Blueprint
from app.controllers import sales_controller

bp = Blueprint('sales', __name__)

bp.route('/sales', methods=['GET', 'POST'])(sales_controller.sales)
bp.route('/sale_register', methods=['POST'])(sales_controller.sale_register)
bp.route('/remove_vehicle/<int:id_veiculo>', methods=['POST'])(sales_controller.remove_vehicle)