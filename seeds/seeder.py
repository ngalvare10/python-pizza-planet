from time import strptime
from flask_seeder import Seeder, Faker, generator
from app.repositories.models import Ingredient, Size, OrderDetail, OrderBeverage, Order, Beverage
from datetime import datetime


class IngredientSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=Ingredient,
      init={
        "_id": generator.Sequence(),
        "name": generator.String("(pepperoni|jamon|anchoas|cebolla|salchicha|carne|pollo|pimiento|pinia|aceitunas)"),
        "price": generator.Integer(start=1, end=10)
      }
    )
    for ingredient in faker.create(10):
        self.db.session.add(ingredient)

class BeverageSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=Beverage,
      init={
        "_id": generator.Sequence(),
        "name": generator.String("(Coca Cola|Pepsi|Agua|Fuze Tea|Fanta|Sprite|Seven Up|Inka|Manzana|Fiora)"),
        "price": generator.Integer(start=1, end=10)
      }
    )
    for ingredient in faker.create(10):
        self.db.session.add(ingredient)

class SizeSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=Size,
      init={
        "_id": generator.Sequence(),
        "name": generator.String("(grande|mediana|pequenia|extra grande|personal)"),
        "price": generator.Integer(start=1, end=10)
      }
    )
    for size in faker.create(5):
        self.db.session.add(size)

class OrderDetailSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=OrderDetail,
      init={
        "_id": generator.Sequence(),
        "ingredient_price": generator.Integer(start=1, end=10),
        "order_id": generator.Integer(start=1, end=100),
        "ingredient_id": generator.Integer(start=1, end=10)
      }
    )
    for detail in faker.create(30):
        self.db.session.add(detail)

class OrderBeverageSeeder(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=OrderBeverage,
      init={
        "_id": generator.Sequence(),
        "beverage_price": generator.Integer(start=1, end=10),
        "order_id": generator.Integer(start=1, end=100),
        "beverage_id": generator.Integer(start=1, end=10)
      }
    )
    for detail in faker.create(30):
        self.db.session.add(detail)

class OrderSeederFirst(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=Order,
      init={
        "_id": generator.Sequence(start=1, end=50),
        "client_name": generator.Name(),
        "client_dni": generator.String("09876543-[0-9][0-9]"),
        "client_address": generator.Email(),
        "client_phone": generator.String("0[0-9]{8}"),
        "date": datetime.strptime("2022-02-10 12:12:12", '%Y-%m-%d %H:%M:%S'), # datetime.strptime("2022-09-22 01:14:27" ,'%Y-%m-%d %H:%M:%S'), #2022-09-22 01:14:27.459896
        "total_price": generator.Integer(start=1, end=50),
        "size_id": generator.Integer(start=1, end=5)
      }
    )
    for order in faker.create(50):
        self.db.session.add(order)

class OrderSeederSecond(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=Order,
      init={
        "_id": generator.Sequence(start=51, end=60),
        "client_name": generator.Name(),
        "client_dni": generator.String("09876543-[0-9][0-9]"),
        "client_address": generator.Email(),
        "client_phone": generator.String("0[0-9]{8}"),
        "date": datetime.strptime("2022-04-10 12:12:12", '%Y-%m-%d %H:%M:%S'),
        "total_price": generator.Integer(start=1, end=50),
        "size_id": generator.Integer(start=1, end=5)
      }
    )
    for order in faker.create(10):
        self.db.session.add(order)

class OrderSeederThird(Seeder):

  # run() will be called by Flask-Seeder
  def run(self):
    faker = Faker(
      cls=Order,
      init={
        "_id": generator.Sequence(start=61, end=100),
        "client_name": generator.Name(),
        "client_dni": generator.String("09876543-[0-9][0-9]"),
        "client_address": generator.Email(),
        "client_phone": generator.String("0[0-9]{8}"),
        "date": datetime.strptime("2022-08-10 12:12:12", '%Y-%m-%d %H:%M:%S'),
        "total_price": generator.Integer(start=1, end=50),
        "size_id": generator.Integer(start=1, end=5)
      }
    )
    for order in faker.create(40):
        self.db.session.add(order)
