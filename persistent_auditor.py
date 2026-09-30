def load_inventory():
    inventory = []

    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split(",")

                    order_id = int(parts[0])
                    product_name = parts[1]
                    quantity = int(parts[2])

                    inventory.append([order_id, product_name, quantity])

    except FileNotFoundError:
        pass

    return inventory

def save_inventory(inventory):
    with open("inventory.txt", "w") as file:
        for i in inventory:
            file.write(f"{i[0]}, {i[1]}, {i[2]}\n")


inventory = load_inventory()

print("Current Orders:")
print()

for i in inventory:
    print(f"{i[0]}, {i[1]}, {i[2]}")

print()

product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))

if inventory:
    new_order_id = inventory[-1][0] + 1
else:
    new_order_id = 1001

new_order = [new_order_id, product_name, quantity]

inventory.append(new_order)

print()
print("New Order Added:")
print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")

save_inventory(inventory)

print()
print("Order successfully saved to inventory.txt")