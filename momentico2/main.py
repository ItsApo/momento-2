class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, product_name, product_description, cost_price, quantity, profit_margin):
        selling_price = cost_price / (1 - profit_margin)
        product = {
            "product_id": product_id,
            "product_name": product_name,
            "product_description": product_description,
            "cost_price": cost_price,
            "quantity": quantity,
            "selling_price": selling_price
        }
        self.inventory[product_id] = product

    def list_products(self):
        for product_id, product in self.inventory.items():
            print(f"Product ID: {product['product_id']}")
            print(f"Product Name: {product['product_name']}")
            print(f"Description: {product['product_description']}")
            print(f"Cost Price: {product['cost_price']}")
            print(f"Quantity: {product['quantity']}")
            print(f"Selling Price: {product['selling_price']}")
            print("\n")


if __name__ == '__main__':
    inventory_manager = InventoryManager()

    inventory_manager.add_product(1, "Product X", "Description X", 15.0, 40, 0.2)
    inventory_manager.add_product(2, "Product Y", "Description Y", 25.0, 20, 0.25)

    inventory_manager.list_products()
