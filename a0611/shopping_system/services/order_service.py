import csv
from models.order import Order

def read_orders():
  orders = []
  with open('data/orders.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
      try:
        order = Order(order_id = row['order_id'],
        customer = row['customer'],
        product = row['product'],
        quantity = int(row['quantity']),
        price = float(row['price']))
        orders.append(order)
      except ValueError:
        print("에러 발생: → 해당 줄은 건너뜁니다.")

  return orders

def calculate_customer_totals(orders):
  totals = {}
  for order in orders:
    if order.customer in totals:
      totals[order.customer] += order.total
    else:
      totals[order.customer] = order.total

  return totals

def calculate_product_quantities(orders):
  quantities = {}
  for order in orders:
    if order.product in quantities:
      quantities[order.product] += order.quantity
    else:
      quantities[order.product] = order.quantity
  return quantities

def get_revenue(item):
  return item[1]

def calculate_product_revenue(orders):
  revenue = {}
  for order in orders:
    if order.product in revenue:
      revenue[order.product] += order.total_price
    else:
      revenue[order.product] = order.total_price

    sorted_revenue = dict(sorted(revenue.items(), key = get_revenue, reverse = True))
    return sorted_revenue
