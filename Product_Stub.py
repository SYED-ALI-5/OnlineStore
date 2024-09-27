class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      total_price = quantity * self.price
      if quantity >= 10 and quantity < 100:
          discount = self.price * 10/100
          total_price = total_price - discount
      elif quantity >= 100:
          discount = self.price * 20/100
          total_price = total_price - discount
      return total_price
  
  def make_purchase(self, quantity):
      pass  

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase