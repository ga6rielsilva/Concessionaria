from flask import Blueprint
from app.controllers import reports_controller

bp = Blueprint('reports', __name__)

bp.route('/reports', methods=['GET'])(reports_controller.reports)