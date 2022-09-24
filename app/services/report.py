from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import OrderController
from app.utils.report_utils import most_revenued_month,most_request_ingredient,better_customers


report = Blueprint('report', __name__)


@report.route('/ingredient', methods=GET)
def get_ingredients():
    orders = OrderController.get_all()
    if len(orders[0]) != 0:
        orders, error = most_request_ingredient(OrderController.get_all())
        response = orders if not error else {'error': error}
        status_code = 200 if orders else 404 if not error else 400
        return jsonify(response), status_code
    else:
        return jsonify([]), 200


@report.route('/month', methods=GET)
def get_months():
    orders = OrderController.get_all()
    if len(orders[0]) != 0:
        orders, error = most_revenued_month(OrderController.get_all())
        response = orders if not error else {'error': error}
        status_code = 200 if orders else 404 if not error else 400
        return jsonify(response), status_code
    else:
        return jsonify([]), 200


@report.route('/customers', methods=GET)
def get_customers():
    orders = OrderController.get_all()
    if len(orders[0]) != 0:
        orders, error = better_customers(OrderController.get_all())
        response = orders if not error else {'error': error}
        status_code = 200 if orders else 404 if not error else 400
        return jsonify(response), status_code
    else:
        return jsonify([]), 200
