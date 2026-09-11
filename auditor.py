inventory = 0

while True:
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        break
    elif not stock.isdigit():
        print("Please enter an integer.")
        continue

    stock = int(stock)

    if stock < 0:
        print("Please enter a positive integer")
        continue

    inventory += stock

    if inventory > 500:
        print("ALERT: Inventory has exceeded 500 units")
        break