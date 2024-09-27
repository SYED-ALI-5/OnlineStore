class OutOfStockError(Exception):
  def __init__(self, message="The Quantity which you want to Purchase is not available in our stock. Sorry for Inconvinience."):
    self.message = message
    super().__init__(self.message)

class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      pass
  
  def make_purchase(self, quantity):
    if quantity > self.amount:
        raise OutOfStockError(f"{quantity} {self.name} is not in stock. In stock items: {self.amount}")
    else:
        self.amount = self.amount - quantity
        price = self.get_price(quantity)
        print(price) 
