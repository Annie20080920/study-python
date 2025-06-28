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

    # if/else 를 한줄로 쓰고 싶다면 get() 활용 가능
    # dict.get(key, default)
    #   - key: 찾고자 하는 키
    #   - default: 키가 존재하지 안흘 경우 반환할 값

    # totals[order.customer_name] = totals.get(order.customer_name, 0) + order.total_price()

  return totals

def calculate_product_quantities(orders):
  quantities = {}
  for order in orders:
    if order.product in quantities:
      quantities[order.product] += order.quantity
    else:
      quantities[order.product] = order.quantity

    # calculate_customer_totals()와 동일하게 get 사용가능
    #quantities[order.product] = order.get(order.product, 0) + order.quantity
  return quantities

def calculate_product_revenue(orders):
  revenue = {}
  for order in orders:
    if order.product in revenue:
      revenue[order.product] += order.total_price()
    else:
      revenue[order.product] = order.total_price()
  # calculate_customer_totals()와 동일하게 get 사용가능
  revenue[order.product] = revenue.get(order.product, 0) + order.total_price()

  sorted_revenue = dict(sorted(revenue.items(), key = lambda item: item[1], reverse = True))

  # Dictionary
  #  - Dictionary는 key, value로 이루어진 쌍으로 원래 순서가 없음.
  #  - 그래서 그냥 출력한다면 오름차순, 내림차순 불가능.

  # Dictionary Sorting
  # - Dictionary타입을 정렬하기 위해서는 sorted() 함수를 쓰면 됨.
  # - sorted()는 새롭게 정렬된 리스트를 반환할 뿐 원본데이터는 바꾸지 않음.
  # - sorted(iterable객체/정렬대상, key=정렬기준키, reverse=오름차순(false)/내림차순(true))
  # - 'key = lambda item: item[1]' 인 이유는 딕셔너리에서 value가 item[1]에 있기 때문에 value기준으로 정렬하기 위해서는 item[1]로 해야함. 
  # - 그럼 이름이 아니라 key기준으로 정렬하고 싶다면? item[0] 쓰면 됨.

  # Lambda
  # - 익명 함수(이름 없는 함수)
  # - 언제 사용할까? => 딱 한번만 쓸 함수라서 굳이 def로 이름 붙이기 귀찮을 때 사용

  return sorted_revenue
