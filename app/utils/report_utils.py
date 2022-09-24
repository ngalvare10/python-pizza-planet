

def most_request_ingredient(orders):
        dicc = {}
        for a in orders[0]:
            ls = a.pop('detail', [])
            for i in ls:
                ingredient = i.get("ingredient").get("name")
                if ingredient not in dicc.keys():
                    dicc[ingredient] = 1
                else:
                    dicc[ingredient] = dicc[ingredient] + 1
        sort_ingredients = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
        return dict([sort_ingredients[0]]), None   


def most_revenued_month(orders):
        dicc = {}
        for a in orders[0]:
            date = a.pop('date', [])
            date = date.split('-')[1]
            total_price = a.pop('total_price', [])
            if date not in dicc.keys():
                dicc[date] = total_price
            else:
                dicc[date] = dicc[date] + total_price
        sort_ingredients = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
        return dict([sort_ingredients[0]]), None    

def better_customers(orders):
        dicc = {}
        for a in orders[0]:
            client_dni = a.pop('client_dni', [])
            client_name = a.pop('client_name', [])
            total_price = a.pop('total_price', [])
            if client_dni not in dicc.keys():
                dicc[client_dni] = [client_name, total_price]
            else:
                dicc[client_dni] = [client_name, dicc[client_dni][1] + total_price]
        sort_ingredients = sorted(dicc.items(), key=lambda x: x[1][1], reverse=True)
        if len(sort_ingredients) > 3:
            return dict(sort_ingredients[0:3]), None
        else: return dict(sort_ingredients), None
    