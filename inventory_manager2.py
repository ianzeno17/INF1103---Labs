
import json
import os

from product import Product
from inventory import Inventory


print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = Inventory()


def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found.")
        print("Starting with sample inventory.")

        inventory.add_product(
            Product("P001", "Laptop", 1200.00, 15)
        )
        inventory.add_product(
            Product("P002", "Mouse", 25.50, 40)
        )
        inventory.add_product(
            Product("P003", "Keyboard", 45.00, 25)
        )


def save_inventory():
    print("Saving inventory...")

    data = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json")


def add_product():
    print("Add New Product")

    product_id = input("Product ID: ").strip()

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Product Name: ").strip()

    if not product_name:
        print("Product name cannot be empty.")
        return

    try:
        product_price = float(input("Price: "))
        product_stock = int(input("Stock Quantity: "))

        if product_price < 0 or product_stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid price and stock quantity.")
        return

    product = Product(
        product_id,
        product_name,
        product_price,
        product_stock
    )

    inventory.add_product(product)

    print("Product added successfully!")


def update_stock():
    print("Update Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is not None:
        print("Product Found:")
        print(f"Name: {product.get_name()}")
        print(f"Current Stock: {product.get_stock()}")

        try:
            new_stock = int(input("New Stock Quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid whole number.")
            return

        product.update_stock(new_stock)
        print("Stock updated successfully!")

    else:
        print("Product not found.")


def search_product():
    print("Search Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is not None:
        print("Product Found")
        print("------------------------------------------------")
        product.display_information()
        print("------------------------------------------------")

    else:
        print("Product not found.")


def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


load_inventory()

while True:
    display_menu()

    try:
        option = int(input("Enter option: "))

    except ValueError:
        print("Please enter a valid option.")
        continue

    if option == 1:
        inventory.display_all()

    elif option == 2:
        add_product()

    elif option == 3:
        update_stock()

    elif option == 4:
        search_product()

    elif option == 5:
        save_inventory()

    elif option == 6:
        print("Saving inventory before exit...")
        save_inventory()
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Please enter a valid option.")