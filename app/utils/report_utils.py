

def most_request_ingredient(orders):
    dicc = {}
    sort_ingredients = {}
    for order in orders[0]:
        ingredients = order.pop('detail', [])
        if len(ingredients) != 0:
            for ingredient in ingredients:
                ingredient = ingredient.get("ingredient").get("name")
                if ingredient not in dicc.keys():
                    dicc[ingredient] = 1
                else:
                    dicc[ingredient] = dicc[ingredient] + 1
            sort_ingredients = sorted(
                dicc.items(), key=lambda x: x[1], reverse=True)
            sort_ingredients = dict([sort_ingredients[0]])
    return sort_ingredients, None


def most_revenued_month(orders):
    dicc = {}
    sort_ingredients = {}
    for order in orders[0]:
        date = order.pop('date', [])
        if len(date) != 0:
            date = date.split('-')[1]
            total_price = order.pop('total_price', [])
            if date not in dicc.keys():
                dicc[date] = total_price
            else:
                dicc[date] = dicc[date] + total_price
            sort_ingredients = sorted(
                dicc.items(), key=lambda x: x[1], reverse=True)
            sort_ingredients = dict([sort_ingredients[0]])

    return sort_ingredients, None


def better_customers(orders):
    dicc = {}
    for order in orders[0]:
        client_dni = order.pop('client_dni', [])
        client_name = order.pop('client_name', [])
        total_price = order.pop('total_price', [])
        if client_dni not in dicc.keys():
            dicc[client_dni] = [client_name, total_price]
        else:
            dicc[client_dni] = [client_name, dicc[client_dni][1] + total_price]
    sort_ingredients = sorted(
        dicc.items(),
        key=lambda x: x[1][1],
        reverse=True)
    if len(sort_ingredients) > 3:
        return dict(sort_ingredients[0:3]), None
    else:
        return dict(sort_ingredients), None
