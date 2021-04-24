class Compare:
    def __init__(self, products):
        if len(products) == 0:
            raise ValueError("Empty list!")
        self._products = products

    def best(self):
        best_product = self._products[0]

        for index in range(1, len(self._products)):
            product = self._products[index]
            if product.grams_value < best_product.grams_value:
                best_product = product

        return best_product
