"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError


@pytest.fixture
def test_item():
    return Item("test", 89.90, 20)


@pytest.fixture(autouse=True, scope='module')
def reset_item_pay_rate():
    Item.pay_rate = 1


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 1798.0


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 89.9
    Item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 80.91


def test_name(test_item):
    test_item.name = "Смартфон"
    assert test_item.name == "Смартфон"
    test_item.name = "СуперСмартфон"
    assert test_item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[4].name == "Клавиатура"
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("src/items2.csv")


def test_instantiate_csv():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("src/items1.csv")


def test_string_to_number():
    assert Item.string_to_number("3") == 3
    assert Item.string_to_number("3.2") == 3
    assert Item.string_to_number("3.8") == 3


def test_repr(test_item):
    assert repr(test_item) == "Item('test', 89.9, 20)"


def test_str(test_item):
    assert str(test_item) == 'test'


def test_add(test_item):
    assert test_item + test_item == 40
