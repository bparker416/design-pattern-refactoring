Test Case 1 curl cmd:
curl -X PUT http://localhost:5002/inventory/Laptop `
     -H "Content-Type: application/json" `
     -d '{ "quantity": 5 }'

Test Case 2 curl cmd:
curl -X GET http://localhost:5002/inventory/Laptop

Test Case 3 curl cmd:
curl -X POST http://localhost:5000/checkout -H "Content-Type: application/json" -d '{ "item": "Laptop", "quantity": 2, "method": "credit_card", "amount": 2000 }'