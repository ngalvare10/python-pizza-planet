from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..controllers import IngredientController
from ..utils.ingredient_decorator import entities_wrapper

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
@entities_wrapper
def create_ingredient():
    return IngredientController.create(request.json)


@ingredient.route('/', methods=PUT)
@entities_wrapper
def update_ingredient():
    return IngredientController.update(request.json)


@ingredient.route('/id/<_id>', methods=GET)
@entities_wrapper
def get_ingredient_by_id(_id: int):
    return IngredientController.get_by_id(_id)


@ingredient.route('/', methods=GET)
@entities_wrapper
def get_ingredients():
    return IngredientController.get_all()
