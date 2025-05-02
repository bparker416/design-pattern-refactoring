# Grocery Software System Refactoring Project

## Overview

This project demonstrates the analysis and refactoring of a grocery software system with three core components: **Cart**, **Payment**, and **Inventory**. The original code implemented common but suboptimal design patterns. Based on a provided business scenario, each component was analyzed for inefficiencies and refactored using more appropriate and maintainable design patterns.

## Components and Design Patterns

| Component | Original Pattern | Refactored Pattern | Justification |
|-----------|------------------|--------------------|---------------|
| Cart      | Singleton         | Model-View-Controller (MVC) | Allows multi-user support and separation of concerns. |
| Payment   | Factory Method    | Strategy           | Enables flexible addition of payment methods without modifying core logic. |
| Inventory | Strategy          | Repository         | Simplifies CRUD operations and aligns with domain-driven design. |

## Refactored Code Structure

### 📦 `cart_mvc.py`
Implements the **MVC Pattern** with:
- `CartModel` for data storage
- `CartView` for output logic
- `CartController` for operations

### 💳 `payment_strategy.py`
Implements the **Strategy Pattern**:
- Abstract base class `PaymentStrategy`
- Concrete strategies: `CreditCardPayment`, `PayPalPayment`
- `PaymentProcessor` context class delegates payment logic

### 🏬 `inventory_repository.py`
Implements the **Repository Pattern**:
- `InventoryRepository` encapsulates stock management methods
- Supports easy extension to persistent storage if needed

## UML Diagrams

UML class diagrams are included to visualize:
- Original vs Refactored design patterns
- Class relationships and responsibilities

## Learning Objectives

✅ Analyze and critique common design patterns  
✅ Refactor legacy code to improve flexibility and scalability  
✅ Apply best-fit software architecture principles  
✅ Communicate technical changes through documentation and diagrams

## How to Run

```bash
# Run the cart controller example
python cart_mvc.py

# Run the payment strategy demo
python payment_strategy.py

# Run the inventory repository test
python inventory_repository.py
