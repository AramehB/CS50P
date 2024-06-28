from numb3rs import validate


def test_string():
    assert validate("cat") == False
    assert validate("banana") == False

def test_large_numbers():
    assert validate("127.127.127.127.127") == False
    assert validate("127.127") == False
    assert validate("127.127.127.127.127.111.222") == False
    assert validate("127.999.127.127") == False

def test_real():
    assert validate("1.1.1.1") == True
    assert validate("100.100.100.100") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
