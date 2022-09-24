from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import OrderController

report = Blueprint('report', __name__)


@report.route('/ingredient', methods=GET)
def get_ingredients():
    orders, error = OrderController.most_request_ingredient()
    response = orders if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/month', methods=GET)
def get_months():
    orders, error = OrderController.most_revenued_month()
    response = orders if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/customers', methods=GET)
def get_customers():
    orders, error = OrderController.better_customers()
    response = orders if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code
