import pytest

from app.controllers import OrderController
from ..utils.functions import get_random_price

from ..utils.functions import (get_random_sequence,
                               get_random_string)


@pytest.fixture
def report_ingredients_uri():
    return '/report/ingredient'


@pytest.fixture
def report_month_uri():
    return '/report/month'


@pytest.fixture
def report_customers_uri():
    return '/report/customers'


@pytest.fixture
def ingredient_result():
    return {"aceitunas":9}


@pytest.fixture
def clients_report() -> dict:
    return [{
        'client_address': get_random_string(),
        'client_dni': "0987654321",
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    },{
        'client_address': get_random_string(),
        'client_dni': "0987654322",
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    },{
        'client_address': get_random_string(),
        'client_dni': "0987654323",
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    },{
        'client_address': get_random_string(),
        'client_dni': "0987654324",
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    },{
        'client_address': get_random_string(),
        'client_dni': "0987654325",
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }]


@pytest.fixture
def ingredients_order():
    return [
        {
        'name': "Jamon",
        'price': get_random_price(10, 20)
    }, {
        'name': "Pepperoni",
        'price': get_random_price(10, 20)
    }, {
        'name': "Salchicha",
        'price': get_random_price(10, 20)
    }
    ]


@pytest.fixture
def orders():
    return OrderController.get_all()
