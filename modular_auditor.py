inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        print("Total Units Processed", inventory)
        print("Number of Failed/Rejected Entries:", failed_entries)
        break
    elif not stock.isdigit():
        print("Please enter an integer.")
        failed_entries += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Please enter a positive integer")
        failed_entries += 1
        continue

    inventory += stock

    if inventory > 500:
        print("ALERT: Inventory has exceeded 500 units")
        break


def get_valid_input():
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        return "quit"

    if not stock.isdigit():
        print("Please enter an integer.")
        return None

    return int(stock)