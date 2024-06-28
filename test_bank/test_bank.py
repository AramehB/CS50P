from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("hi") == 20
    assert value("howdy") == 20
    assert value("hows it goin?") == 20

def test_not_start_with_h():
    assert value("Good morning") == 100
    assert value("Sup") == 100
    assert value("yo") == 100
