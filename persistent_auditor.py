def get_valid_input():
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        return "quit"

    if not stock.isdigit():
        print("Please enter an integer.")
        return None

    return int(stock)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        generate_report(deliveries_processed, failed_entries)
        break
    elif stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)
    print("Tax:", tax)

    deliveries_processed += 1

    if inventory > 500:
        print("ALERT: Inventory has exceeded 500 units")
        break