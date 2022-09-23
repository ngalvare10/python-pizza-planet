from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)


@beverage.route('/', methods=POST)
def create_Beverage():
    Beverage, error = BeverageController.create(request.json)
    response = Beverage if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@beverage.route('/', methods=PUT)
def update_Beverage():
    Beverage, error = BeverageController.update(request.json)
    response = Beverage if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@beverage.route('/id/<_id>', methods=GET)
def get_Beverage_by_id(_id: int):
    Beverage, error = BeverageController.get_by_id(_id)
    response = Beverage if not error else {'error': error}
    status_code = 200 if Beverage else 404 if not error else 400
    return jsonify(response), status_code


@beverage.route('/', methods=GET)
def get_Beverages():
    Beverages, error = BeverageController.get_all()
    response = Beverages if not error else {'error': error}
    status_code = 200 if Beverages else 404 if not error else 400
    return jsonify(response), status_code
