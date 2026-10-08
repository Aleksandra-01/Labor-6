 from abc import ABC, abstractmethod

   class PaymentMethod(ABC):
       @abstractmethod
       def pay(self, amount):
           pass
        class CardPayment(PaymentMethod):
       def pay(self, amount):
           return f"Оплата картой: {amount} тг"


   class CashPayment(PaymentMethod):
       def pay(self, amount):
           return f"Оплата наличными: {amount} тг" 
        class Order:
       def __init__(self, payment_method):
           self.payment_method = payment_method

       def checkout(self, amount):
           return self.payment_method.pay(amount)
        order = Order(CardPayment())
   print(order.checkout(5000))
 order = Order(CashPayment())
   print(order.checkout(5000))
class PaymentMethod:
    def pay(self): ...
    def refund(self): ...
    def print_receipt(self): ...
    def save_to_database(self): ...
    def send_email(self): ...
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass