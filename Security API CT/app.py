from flask import Flask
from database import db
from schemas import ma
from limiter import limiter
from caching import cache

from models.user import User

from routes.customerBP import customer_blueprint
from routes.employeeBP import employee_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint
from routes.loginBP import login_blueprint


def create_app(config_name):
    app = Flask(__name__)
