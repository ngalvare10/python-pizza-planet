from app.common.http_methods import GET
from flask import Blueprint

from ..controllers import OrderController
from app.utils.report_utils import (most_revenued_month,
                                    most_request_ingredient, better_customers)
from ..utils.ingredient_decorator import entities_wrapper

report = Blueprint('report', __name__)


@report.route('/ingredient', methods=GET)
@entities_wrapper
def get_ingredients():
    return most_request_ingredient(OrderController.get_all())


@report.route('/month', methods=GET)
@entities_wrapper
def get_months():
    return most_revenued_month(OrderController.get_all())


@report.route('/customers', methods=GET)
@entities_wrapper
def get_customers():
    return better_customers(OrderController.get_all())
