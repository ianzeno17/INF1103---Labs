import json
import os

inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
       "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25 
    }
]


def display_all():
    print("Current Inventory")
    print("------------------------------------------------")

    for i in inventory:
        print(f"ID: {i['id']} | Name: {i['name']} | Price: ${i['price']:.2f} | Stock: {i['stock']}")

    print("------------------------------------------------")

def add_product():
    print("Add New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    product_price = float(input("Price: "))
    product_stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "stock": product_stock
    }

    inventory.append(new_product)

    print("Product added successfully!")

add_product()
display_all()