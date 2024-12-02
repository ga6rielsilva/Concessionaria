from flask import Blueprint
from app.controllers import settings_controller

bp = Blueprint('settings', __name__)

bp.route('/settings', methods=['GET', 'POST'])(settings_controller.settings)