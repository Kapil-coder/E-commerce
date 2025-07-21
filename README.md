# E-commerce Backend with FastAPI & MongoDB

This is my beginner backend project built while learning FastAPI and MongoDB. It has simple APIs to create products, place orders, and get order history like Amazon/Flipkart.

##  Tech Stack

-  **FastAPI** — Modern, fast (high-performance) web framework
-  **MongoDB Atlas** — Cloud-hosted NoSQL database
-  **PyMongo** — Native MongoDB driver for Python
-  **python-dotenv** — Environment variable management
-  **Thunder Client** — API testing (like Postman)

# Features

| Feature            | Method | Endpoint               | Description                          |
|--------------------|--------|------------------------|--------------------------------------|
|   Create Product   | POST   | `/products`            | Add a new product                    |
|   List Products    | GET    | `/products`            | List and filter products             |
|   Create Order     | POST   | `/orders`              | Create order for a user              |
|   List User Orders | GET    | `/orders/{user_id}`    | Get orders for a specific user       |

Supports filtering, regex search, pagination (`limit`, `offset`).


## Product API

### `POST /products`

{
  "name": "T-Shirt",
  "price": 499.99,
  "sizes": [
    { "size": "M", "quantity": 50 }
  ]
}

GET /products?name=shirt&size=M
Returns products matching filters.


## Orders API

### POST /orders

{
  "user_id": "kapil123",
  "product_ids": ["<id1>", "<id2>"]
}

GET /orders/kapil123?limit=2&offset=0
Returns all orders of user kapil123.









