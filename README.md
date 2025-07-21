# E-commerce Backend with FastAPI & MongoDB

This is a sample backend project built using **FastAPI** and **MongoDB Atlas**

It demonstrates CRUD APIs for an e-commerce-like system, including product listing, order creation, and user-specific order history.

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

```json
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









