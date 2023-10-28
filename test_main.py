import pytest
from main import square, division

def test_positive():
    assert square(2) == 4
    assert square(4) == 16

def test_zero():
    assert square(0) == 0

def test_negative():
    assert square(-2) == 4
    assert square(-4) == 16

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_division():
    assert division(7, 14) == 0.5

def test_divide_by_zero():
    assert division(5, 0) == "Divisor can't be zero"
