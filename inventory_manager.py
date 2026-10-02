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

def search_product():
    print("Search Product")
    search_id = input("Enter Product ID: ")

    for i in inventory:
        if i["id"] == search_id:
            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {i['id']}")
            print(f"Name: {i['name']}")
            print(f"Price: ${i['price']:.2f}")
            print(f"Stock: {i['stock']}")
            print("------------------------------------------------")
            return
        
    print("Product not found.")

def update_stock():
    print("Update Stock")
    add_id = input("Enter Product ID: ")

    for i in inventory:
        if i['id'] == add_id:
            print("Product Found:")
            print(f"Name: {i['name']}")
            print(f"Current Stock: {i['stock']}")

            new_stock = int(input("New Stock Quantity: "))

            i["stock"] = new_stock

            print("Stock updated successfully!")
            return
        
    print("Product not found.")

def load_inventory():
    global inventory

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")

        inventory = []

def save_inventory():
    print("Saving inventory...")

    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json")

save_inventory()