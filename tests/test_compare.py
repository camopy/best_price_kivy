import pytest

from compare import Compare
from product import Product


@pytest.fixture
def product_one():
    return Product("Rice A", 1000, 5.0)


@pytest.fixture
def product_two():
    return Product("Rice B", 5000, 23.0)


@pytest.fixture
def product_three():
    return Product("Rice C", 2000, 11.0)


def test_should_deny_compare_empty_list(product_one):
    with pytest.raises(ValueError):
        Compare([])


def test_should_return_best_price_from_one_product(product_one):
    compare = Compare([product_one])
    assert compare.best() == product_one


def test_should_return_best_price_from_two_product(product_one, product_two):
    compare = Compare([product_one, product_two])
    assert compare.best() == product_two


def test_should_return_best_price_from_three_product(
    product_one, product_two, product_three
):
    compare = Compare([product_one, product_two, product_three])
    assert compare.best() == product_two