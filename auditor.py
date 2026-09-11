inventory = 0

while True:
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        break

    elif not stock.isdigit():
        print("Please enter an integer.")
        
    elif stock < 0:
        print("Please enter a positive integer")
        