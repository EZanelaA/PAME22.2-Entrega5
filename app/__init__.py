from flask import Flask
from .extensions import ma, db, mi, jwt
from .config import Config
from app.employees.routes import employee_api
from app.products.routes import product_api
from app.requests.routes import request_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    ma.init_app(app)
    db.init_app(app)
    mi.init_app(app, db)
    jwt.init_app(app)
    app.register_blueprint(employee_api)
    app.register_blueprint(product_api)
    app.register_blueprint(request_api)
    return app