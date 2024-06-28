
from seasons import get_days_old


def test_days_old():
    assert get_days_old(2000, 1, 1) == 8941          #might have to change depending on the date of testing
