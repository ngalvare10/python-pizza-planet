from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..controllers import OrderController
from ..utils.ingredient_decorator import entities_wrapper

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
@entities_wrapper
def create_order():
    return OrderController.create(request.json)


@order.route('/id/<_id>', methods=GET)
@entities_wrapper
def get_order_by_id(_id: int):
    return OrderController.get_by_id(_id)


@order.route('/', methods=GET)
@entities_wrapper
def get_orders():
    return OrderController.get_all()
