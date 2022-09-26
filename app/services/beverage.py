from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import BeverageController
from ..utils.ingredient_decorator import entities_wrapper

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
@entities_wrapper
def create_Beverage():
    return BeverageController.create(request.json)


@beverage.route('/', methods=PUT)
@entities_wrapper
def update_Beverage():
    return BeverageController.update(request.json)


@beverage.route('/id/<_id>', methods=GET)
@entities_wrapper
def get_Beverage_by_id(_id: int):
    return BeverageController.get_by_id(_id)


@beverage.route('/', methods=GET)
@entities_wrapper
def get_Beverages():
    return BeverageController.get_all()
