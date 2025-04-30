Name: Brandon Parker
Student ID: 000408700
Python Version: Python v3.10

Function Descriptions:
add_item() - Adds an (item, quantity) tuple to the in-memory cart and returns a confirmation JSON.
view_cart() - Return the current cart contents as JSON.
add_stock(item) - Increments available stock for <item> by the quantity in the request body.
get_stock(item) - Retrieves current stock level for <item>.
reserve(item) - Atomically decreases stock if enough units are available; otherwise returns 409.
pay() - Dummy endpoint that "processes" a payment (any method/amount) and echoes a success message.
add_to_inventory(item) - Convenience wrapper that forwards the request to inventory_service.add_stock.
add_to_cart() - Saga step 1: Reserves stock in inventory_service --> on success adds the item to cart_service.
checkout() - Saga step 2: Forward payment details to payment_service; returns its JSON response.

Steps to Run Functions:
Prerequisites:
Open terminal
pip install flask requests
*** Start Each Service in its own terminal ***
python cart_service.py # port 5001
python inventory_service.py # port 5002
python payment_service.py # port 5003
python orchestrator_service.py # port 5000

1. Cart Functions (5001)
# add_item
curl -X POST http://localhost:5002/cart \
     -H "Content-Type: application/json" \
     -d '{ "item": "Laptop", "quantity": 2 }'

# view_cart
curl -X GET http://localhost:5002/cart

2. Inventory Functions (5002)
# add_stock
curl -X PUT http://localhost:5001/inventory/Laptop \
     -H "Content-Type: application/json" \
     -d '{ "quantity": 5 }'

# get_stock
curl -X GET http://localhost:5001/inventory/Laptop

# reserve
curl -X POST http://localhost:5001/inventory/Laptop \
     -H "Content-Type: application/json" \
     -d '{ "quantity": 2 }'

3. Payment Functions (5000)
curl -X POST http://localhost:5003/payment \
     -H "Content-Type: application/json" \
     -d '{ "amount": 2000, "method": "credit_card" }'

4. Orchestrator Functions (5000)
# add_to_inventory (wrapper)
curl -X PUT http://localhost:5000/add_to_inventory/Laptop \
     -H "Content-Type: application/json" \
     -d '{ "quantity": 5 }'

# add_to_cart   (reserve + cart)
curl -X POST http://localhost:5000/add_to_cart \
     -H "Content-Type: application/json" \
     -d '{ "item": "Laptop", "quantity": 2 }'

# checkout      (payment)
curl -X POST http://localhost:5000/checkout \
     -H "Content-Type: application/json" \
     -d '{ "item": "Laptop", "quantity": 2, "method": "credit_card", "amount": 2000 }'