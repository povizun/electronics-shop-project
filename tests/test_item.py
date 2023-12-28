"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

test_item = Item("test", 89.90, 20)


def test_calculate_total_price():
    assert test_item.calculate_total_price() == 1798.0


def test_apply_discount():
    test_item.apply_discount()
    assert test_item.price == 89.9
    Item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 80.91
