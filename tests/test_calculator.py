from utils.calculator import add, sub, mul, div, calculate
import math
import pytest


def test_basic_ops():
    assert add(2, 3) == 5
    assert sub(10, 4) == 6
    assert mul(3, 5) == 15
    assert div(9, 3) == 3


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_calculate_strings():
    assert calculate("3+4") == 7
    assert math.isclose(calculate("10/4"), 2.5, rel_tol=1e-9)
    assert calculate("6*7") == 42


def test_calculate_invalid():
    import pytest
    with pytest.raises(ValueError):
        calculate("3 ^ 4")
