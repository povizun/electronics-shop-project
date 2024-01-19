import pytest

from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone("test", 89.90, 20, 1)


def test_repr(test_phone):
    assert repr(test_phone) == "Phone('test', 89.9, 20, 1)"


def test_str(test_phone):
    assert str(test_phone) == 'test'


def test_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 1
    test_phone.number_of_sim = 2
    assert  test_phone.number_of_sim == 2


def test_add(test_phone):
    assert test_phone + test_phone == 40
