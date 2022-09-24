import pytest
import random
from datetime import datetime

from app.controllers import (IngredientController, OrderController,
                             SizeController, BeverageController)
from app.controllers import OrderController
from app.controllers.base import BaseController

from app.utils.report_utils import most_revenued_month,most_request_ingredient,better_customers

def __order(ingredients: list, size: dict,client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    size_id = size.get('_id')
    date_init = datetime(2022, 1, 1)
    date_final =  datetime(2022, 12, 31)
    random_date = date_init + (date_final - date_init) * random.random()
    return {
        **client_data,
        'date': random_date,
        'ingredients': ingredients,
        'size_id': size_id
    }

def __create_items(items: list,  controller: BaseController):
    created_items = []
    for ingredient in items:
        created_item, _ = controller.create(ingredient)
        created_items.append(created_item)
    return created_items

def __create_sizes_and_ingredients(ingredients: list, sizes: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_sizes = __create_items(sizes, SizeController)
    return created_sizes if len(
        created_sizes) > 1 else created_sizes.pop(), created_ingredients

def __create_orders(app, ingredients, size, clients_report):
    list_orders = []
    for _ in range(10):
        created_size, created_ingredients = __create_sizes_and_ingredients(ingredients, [size])
        order = __order([random.choice(created_ingredients)], created_size, random.choice(clients_report))
        created_order, error = OrderController.create(order)
        list_orders.append(created_order)
    return list_orders

def __create_orders_no_ingredients(app, size, clients_report):
    list_orders = []
    for _ in range(10):
        created_size, created_ingredients = __create_sizes_and_ingredients([], [size])
        order = __order(created_ingredients, created_size, random.choice(clients_report))
        created_order, error = OrderController.create(order)
        list_orders.append(created_order)
    return list_orders

def test_most_request_ingredient(app, ingredients, size, clients_report):
    list_orders = __create_orders(app, ingredients, size, clients_report)
    pytest.assume(most_request_ingredient([list_orders])[0] != None)

def test_most_request_no_ingredient(app, size, clients_report):
    list_orders = __create_orders_no_ingredients(app, size=size, clients_report=clients_report)
    pytest.assume(most_request_ingredient([list_orders])[0] == "No ingredients in orders")

def test_most_revenued_month(app, ingredients, size, clients_report):
    list_orders = __create_orders(app, ingredients, size, clients_report)
    pytest.assume(most_revenued_month([list_orders])[0] != None)

def test_better_customers(app, ingredients, size, clients_report):
    list_orders = __create_orders(app, ingredients, size, clients_report)
    pytest.assume(better_customers([list_orders])[0] != None)

