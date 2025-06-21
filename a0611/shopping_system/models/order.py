class Order:
  def __init__(self, order_id, customer_name, product, quantity, price):
    try:
      self.order_id = int(order_id)
      self.customer_name = customer_name
      self.product = product
      self.quantity = int(quantity)
      self.price = float(price)
    
    except ValueError:
      raise ValueError ("에러 발생: → 해당 줄은 건너뜁니다.")
 
  def total_price(self):
    return self.quantity * self.price