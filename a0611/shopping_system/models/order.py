class Order:
  def __init__(self, order_id, customer, product, quantity, price):
    self.order_id = order_id
    self.customer = customer
    self.product = product
    self.quantity = quantity
    self.price = price

  def total_price(self):
    return self.quantity * self.price