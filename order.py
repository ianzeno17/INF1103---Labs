from order_line import OrderLine
from product import Product


class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_product(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total: float = 0.0

        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        print(f"Order ID: {self.__order_id}")

        for order_line in self.__order_lines:
            product = order_line.get_product()

            print(f"Product: {product.get_name()}")
            print(f"Quantity: {order_line.get_quantity()}")
            print(f"Subtotal: ${order_line.calculate_subtotal():.2f}")

        print(f"Total: ${self.calculate_total():.2f}")