from flask import Blueprint
from app.controllers import index_controller

bp = Blueprint('index', __name__)

bp.route('/home')(index_controller.home)