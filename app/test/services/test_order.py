import pytest

def test_create_order_service(create_orders):
    orders = create_orders[0].json
    a = 1
    pytest.assume(create_orders[0].status.startswith('200'))
    pytest.assume(orders['_id'])
    pytest.assume(orders['client_dni'])
    pytest.assume(orders['client_name'])
    pytest.assume(orders['client_phone'])
    pytest.assume(orders['date'])
    pytest.assume(orders['detail'])
    pytest.assume(orders['detail_beverage'])
    pytest.assume(orders['size'])
    pytest.assume(orders['total_price'])


def test_get_order_by_id_service(client, create_orders, order_uri):
    for current_order in create_orders:
        response = client.get(f'{order_uri}id/{current_order.json["_id"]}')
        pytest.assume(response.status.startswith('200'))
        returned_order = response.json
        for param, value in current_order.json.items():
            pytest.assume(returned_order[param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {
        order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order.json['_id'] in returned_orders)
