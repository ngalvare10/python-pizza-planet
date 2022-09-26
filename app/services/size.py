from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import SizeController
from ..utils.ingredient_decorator import entities_wrapper

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
@entities_wrapper
def create_size():
    return SizeController.create(request.json)


@size.route('/', methods=PUT)
@entities_wrapper
def update_size():
    return SizeController.update(request.json)


@size.route('/id/<_id>', methods=GET)
@entities_wrapper
def get_size_by_id(_id: int):
    return SizeController.get_by_id(_id)


@size.route('/', methods=GET)
@entities_wrapper
def get_sizes():
    return SizeController.get_all()
