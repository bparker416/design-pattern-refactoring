# Snippet 1: Cart Component updated using MVC Pattern
# Changed Singleton to MVC Pattern
# Support multiple users/carts independently

# Model
# CartModel handles data
class CartModel:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

# View
# CartView handles presentation
class CartView:
    @staticmethod
    def display_cart(items):
        for item, quantity in items:
            print(f"{quantity} of {item}(s) in cart.")

# Controller
# CartController handles operations
class CartController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item_to_cart(self, item, quantity):
        self.model.add_item(item, quantity)

    def show_cart(self):
        self.view.display_cart(self.model.items)

# Snippet 2: Payment Component updated using Strategy Pattern
# PaymentProcessor uses any PaymentStrategy dynamically without hardcoding
# Easy to extend new payment methods without modifying existing code

class PaymentStrategy:
    def process_payment(self, amount):
        raise NotImplementedError("You must implement the process_payment method.")

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing credit card payment: {amount}")

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing PayPal payment: {amount}")

# Context class
class PaymentProcessor:
    def __init__(self, strategy: PayPalPayment):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.process_payment(amount)

# Snippet 3: Inventory Component updated using Repository Pattern
# Simplified from Strategy to Repository Pattern
# Repository handles inventory storage and operations
# Easier to manage inventory updates directly

class InventoryRepository:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        self.stock[item] = self.stock.get(item, 0) + quantity
        print(f"Added {quantity} of {item}(s) in inventory.")

    def remove_stock(self, item, quantity):
        if item in self.stock and self.stock[item] >= quantity:
            self.stock[item] -= quantity
            print(f"Removed {quantity} of {item}(s) from inventory.")
        else:
            print(f"No such {item}(s) in inventory.")

    def get_stock(self, item):
        return self.stock.get(item, 0)


































