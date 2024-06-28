from twttr import shorten


def test_title():
    assert shorten("Twitter") == "Twttr"       #our output is the entire string

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("TWITTER1") == "TWTTR1"

def test_punctuation():
    assert shorten("TWITTER,") == "TWTTR,"
