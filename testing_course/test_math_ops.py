import pytest
from math_ops import add, subtract, divide

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(20, 10) == 10

def test_divide_success():
    a = 116
    b = 2
    expected = 116/2

    result = divide(a, b)

    assert result == expected

def test_divide_by_zero():
    a = 25
    b = 0

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(a, b)
