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
