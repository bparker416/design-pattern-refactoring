# Snippet 1: Cart Component updated using MVC Pattern

class Cart:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cart, cls).__new__(cls)
            cls._instance.items = []
        return cls._instance

    def add_item(self, item, quantity):
        self.items.append((item, quantity))
        print(f"Added {quantity} {item}(s) to cart.")




# Snippet 2: Payment Component

class CreditCardProcessor:
    def process_payment(self, amount):
        print(f"Processing {amount} via Credit Card.")

class PayPalProcessor:
    def process_payment(self, amount):
        print(f"Processing {amount} via PayPal.")

class PaymentProcessorFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit_card":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Unsupported payment method.")


# Snippet 3: Inventory Component

class Inventory:
    def __init__(self, strategy):
        self.stock = {}
        self.strategy = strategy

    def add_item(self, item, quantity):
        self.strategy.update_stock(self.stock, item, quantity)

# Two different strategies for inventory updates
class AddStockStrategy:
    def update_stock(self, stock, item, quantity):
        stock[item] = stock.get(item, 0) + quantity
        print(f"Added {quantity} {item}(s) to inventory.")

class RemoveStockStrategy:
    def update_stock(self, stock, item, quantity):
        if item in stock and stock[item] >= quantity:
            stock[item] -= quantity
            print(f"Removed {quantity} {item}(s) from inventory.")
        else:
            print(f"Not enough {item} in stock to remove {quantity} units.")