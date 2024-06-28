from um import count

def test_um():
    assert count("um") == 1
    assert count("Um") == 1

def test_punctuation():
    assert count("um,") == 1
    assert count("um?") == 1
    assert count("um ") == 1

def test_no_um():
    assert count("yum") == 0

def test_sentence():
    assert count("Um, hello, um, how are you?") == 2
