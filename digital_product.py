from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier
    ) -> None:

        super().__init__(
            product_id,
            name,
            price,
            stock,
            supplier
        )

        self.__download_size: float = download_size

    def display_information(self) -> None:
        print(
            f"ID: {self.get_product_id()} | "
            f"Name: {self.get_name()} | "
            f"Price: {self.get_price()} | "
            f"Stock: {self.get_stock()} | "
        )
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def get_download_size(self) -> float:
        return self.__download_size

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data