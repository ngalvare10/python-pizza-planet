import pytest


def test_report_ingredients_service(client, report_ingredients_uri):
    response = client.get(report_ingredients_uri)
    pytest.assume(response.status.startswith('200'))
    

def test_report_month_service(client, report_month_uri):
    response = client.get(report_month_uri)
    pytest.assume(response.status.startswith('200'))
    

def test_report_customers_service(client, report_customers_uri):
    response = client.get(report_customers_uri)
    pytest.assume(response.status.startswith('200'))
    