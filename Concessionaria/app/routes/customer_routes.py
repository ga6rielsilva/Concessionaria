from flask import Blueprint
from app.controllers import customer_controller

bp = Blueprint('customer', __name__)

bp.route('/customer_register', methods=['GET', 'POST'])(customer_controller.customer_register)
bp.route('/customer_search', methods=['GET', 'POST'])(customer_controller.customer_search)
bp.route('/delete_customer/<string:cpf>', methods=['POST'])(customer_controller.delete_customer)
bp.route('/edit_customer/<string:cpf>', methods=['GET', 'POST'])(customer_controller.edit_customer)