from flask import Blueprint
from app.controllers import employee_controller

bp = Blueprint('employee', __name__)

bp.route('/employee_register', methods=['GET', 'POST'])(employee_controller.employee_register)
bp.route('/employee_search', methods=['GET', 'POST'])(employee_controller.employee_search)
bp.route('/delete_employee/<string:cpf>', methods=['POST'])(employee_controller.delete_employee)
bp.route('/edit_employee/<string:cpf>', methods=['GET', 'POST'])(employee_controller.edit_employee)