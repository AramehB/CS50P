import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("2/3") == 67
    assert convert("1/4") == 25
    assert convert("0/3") == 0
    assert convert("95/100") == 95

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(25) == "25%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(95) == "95%"
    assert gauge(99) == "F"

def test_div_by_0():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("5/1")
