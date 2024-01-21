import pytest

from src.keyboard import Keyboard


@pytest.fixture
def test_kb():
    return Keyboard("test", 89.90, 20)


def test_calculate_total_price(test_kb):
    assert test_kb.calculate_total_price() == 1798.0


def test_apply_discount(test_kb):
    test_kb.apply_discount()
    assert test_kb.price == 89.9
    Keyboard.pay_rate = 0.9
    test_kb.apply_discount()
    assert test_kb.price == 80.91


def test_repr(test_kb):
    assert repr(test_kb) == "Keyboard('test', 89.9, 20)"


def test_str(test_kb):
    assert str(test_kb) == 'test'


def test_add(test_kb):
    assert test_kb + test_kb == 40


def test_change_lang(test_kb):
    assert str(test_kb.language) == "EN"

    test_kb.change_lang()
    assert str(test_kb.language) == "RU"

    # Сделали EN -> RU -> EN
    test_kb.change_lang()
    assert str(test_kb.language) == "EN"
