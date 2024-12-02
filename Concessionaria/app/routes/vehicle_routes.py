from flask import Blueprint
from app.controllers import vehicle_controller

bp = Blueprint('vehicle', __name__)

bp.route('/vehicle_register', methods=['GET', 'POST'])(vehicle_controller.vehicle_register)
bp.route('/vehicle_search', methods=['GET', 'POST'])(vehicle_controller.vehicle_search)
bp.route('/delete_vehicle/<string:plate>', methods=['POST'])(vehicle_controller.delete_vehicle)
bp.route('/edit_vehicle/<string:plate>', methods=['GET', 'POST'])(vehicle_controller.edit_vehicle)