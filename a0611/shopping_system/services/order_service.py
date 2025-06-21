import csv
from models.order import Order
from pathlib import Path

def read_orders():
  orders = []
  file_path = Path(__file__).resolve().parent.parent/'data'/'orders.csv'
  
  with open(file_path, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
      try:
        order = Order(
          order_id = row['order_id'],
          customer_name = row['customer_name'],
          product = row['product'],
          quantity = row['quantity'],
          price = row['price']
        )  
        orders.append(order)
      except ValueError:
          print("에러 발생: → 해당 줄은 건너뜁니다.")

  return orders

def calculate_customer_totals(orders):
  totals = {}

  for order in orders:
    if order.customer_name in totals:
      totals[order.customer_name] += order.total_price()
    else:
      totals[order.customer_name] = order.total_price()

  return totals

def calculate_product_quantities(orders):
  quantities = {}
  for order in orders:
    if order.product in quantities:
      quantities[order.product] += order.quantity
    else:
      quantities[order.product] = order.quantity
  return quantities

def calculate_product_revenue(orders):
  revenue = {}
  for order in orders:
    if order.product in revenue:
      revenue[order.product] += order.total_price()
    else:
      revenue[order.product] = order.total_price()

  sorted_revenue = dict(sorted(revenue.items(), key = lambda item: item[1], reverse = True))
  return sorted_revenue
