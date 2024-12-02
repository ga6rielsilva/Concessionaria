from flask import Blueprint
from app.controllers import auth_controller

bp = Blueprint('auth', __name__)

bp.before_request(auth_controller.restrict_access)

bp.route('/', methods=['GET', 'POST'])(auth_controller.login)
bp.route('/logout')(auth_controller.logout)
bp.route('/home')(auth_controller.home)