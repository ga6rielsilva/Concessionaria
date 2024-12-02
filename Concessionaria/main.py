from flask import Flask
from app.database.connection import getDatabaseConnection
from app.routes import (auth_routes, customer_routes, employee_routes, reports_routes, index_routes, sales_routes, settings_routes, vehicle_routes)
from app.controllers.auth_controller import restrict_access

app = Flask(__name__, template_folder='templates')
app.secret_key = 'z/\x9c\x9bO\r\xcb\xec\xa5kSC\x890P(\xf0\xbd\xa2\\K\xf3\x13\xd4'

# Registrar rotas
app.register_blueprint(auth_routes.bp)
app.register_blueprint(customer_routes.bp)
app.register_blueprint(employee_routes.bp)
app.register_blueprint(reports_routes.bp)
app.register_blueprint(index_routes.bp)
app.register_blueprint(sales_routes.bp)
app.register_blueprint(settings_routes.bp)
app.register_blueprint(vehicle_routes.bp)

# Aplicar a função restrict_access globalmente
@app.before_request
def before_request():
    return restrict_access()

if __name__ == '__main__':
    try:
        conn = getDatabaseConnection()
        conn.close()
    finally:
        app.run(debug=True)