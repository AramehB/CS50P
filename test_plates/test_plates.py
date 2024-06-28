from plates import is_valid

def test_num():
    assert is_valid("123456") == False
    assert is_valid("111111") == False
    assert is_valid("999999") == False

def test_alnum():
    assert is_valid("A12345") == False
    assert is_valid("A1KJHA") == False
    assert is_valid("AAA123") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAH056") == False

def test_alpha():
    assert is_valid("ABCDEF") == True
    assert is_valid("ANBSKU") == True
    assert is_valid("VISDNP") == True

def test_punctuation():
    assert is_valid("AA34,6") == False
    assert is_valid("AB123?") == False

def test_number_of_characters():
    assert is_valid("A") == False
    assert is_valid("AA123A4") == False
    assert is_valid("CS50") == True
