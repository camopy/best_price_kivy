class Product:
    def __init__(self, name, grams, price):
        self._name = name
        self._grams = grams
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def grams(self):
        return self._grams

    @property
    def price(self):
        return self._price

    @property
    def grams_value(self):
        return self.price / self.grams
