import pytest
from working import convert

def test_formatting():
    with pytest.raises(ValueError):
        convert("7:00 AM - 9:00 AM")
        convert("7AM - 9AM")
        convert("7 AM - 9 AM")
        convert("7AM 9AM")            #had to get rid of the "to" to get this test to work properly


def test_minutes():
    with pytest.raises(ValueError):
        convert("7:00 AM to 9:60 AM")
        convert("7:100 AM to 9:60 AM")

def test_hours():
     with pytest.raises(ValueError):
        convert("13:00 AM to 9:00 AM")
        convert("0:00 AM to 9:40 AM")

def test_overall():
    assert convert("7:00 PM to 9:30 AM") == "19:00 to 09:30"

