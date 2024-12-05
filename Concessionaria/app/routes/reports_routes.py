from flask import Blueprint
from app.controllers import reports_controller, stockreport_controller

bp = Blueprint('reports', __name__)

# Rota para relatórios
bp.route('/reports', methods=['GET'])(reports_controller.reports)

# Rota para relatório de estoque
bp.route('/reports/stockreport', methods=['GET'])(stockreport_controller.stockreport)