from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from compare import Compare
from product import Product


class ProductComponent(Widget):
    product_a_grid = ObjectProperty(None)
    product_a_label = ObjectProperty(None)
    quantity_a = ObjectProperty(None)
    price_a = ObjectProperty(None)

    product_b_grid = ObjectProperty(None)
    product_b_label = ObjectProperty(None)
    price_b = ObjectProperty(None)
    quantity_b = ObjectProperty(None)

    def best_price(self):
        if self.valid_inputs():
            product_a = Product(
                "Product A", int(self.quantity_a.text), float(self.price_a.text)
            )
            product_b = Product(
                "Product B", int(self.quantity_b.text), float(self.price_b.text)
            )
            compare = Compare([product_a, product_b])
            best_product = compare.best()
            self.highlight_best_product(best_product)

    def highlight_best_product(self, best_product):
        if best_product.name == "Product A":
            self.product_a_label.text = "Product A is cheaper"
            self.product_b_label.text = "Product B"
        else:
            self.product_b_label.text = "Product B is cheaper"
            self.product_a_label.text = "Product A"

    def valid_inputs(self):
        if (
            not self.quantity_a.text
            or not self.quantity_b.text
            or not self.price_a.text
            or not self.price_b.text
        ):
            return False
        return True


class MyApp(App):
    def build(self):
        return ProductComponent()


if __name__ == "__main__":
    MyApp().run()