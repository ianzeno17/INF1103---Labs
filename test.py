from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product


supplier = Supplier(
    "S001",
    "Logitech",
    "support@logitech.com"
)

physical = PhysicalProduct(
    "P001",
    "Mechanical Keyboard",
    89.90,
    20,
    1.2,
    supplier
)

digital = DigitalProduct(
    "P002",
    "Python E-book",
    19.90,
    50,
    25.0,
    supplier
)

print("===== SUPPLIER TEST =====")
print(physical.get_supplier().get_name())


print("\n===== INVENTORY TEST =====")

inventory1 = Inventory()
inventory2 = Inventory()

inventory1.add_product(physical)
inventory1.add_product(digital)

inventory1.display_all()


print("\n===== TRANSFER TEST =====")

removed_product = inventory1.remove_product("P001")

if removed_product is not None:
    inventory2.add_product(removed_product)

print("Inventory 1:")
inventory1.display_all()

print("Inventory 2:")
inventory2.display_all()


print("\n===== ORDER TEST =====")

order = Order("O001")

order.add_product(physical, 2)
order.add_product(digital, 1)

order.display_order()


print("\n===== POLYMORPHISM TEST =====")


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


show_product_details(physical)
show_product_details(digital)


print("\n===== LSP TEST =====")

physical.update_stock(15)
digital.update_stock(40)

print(physical.get_stock())
print(digital.get_stock())