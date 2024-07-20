from project import create_deck, check_winner, get_value

def test_create_deck():
    deck = create_deck()
    assert len(deck) == 52
    assert all(deck.count(card) == 4 for card in ["Ace", "Jack", "Queen", "King", 2, 3, 4, 5, 6, 7, 8, 9, 10])



def test_get_value():
    assert get_value("Jack") == 10
    assert get_value("King") == 10
    assert get_value("Queen") == 10
    assert get_value("Ace") == "1/11"
    assert get_value(10) == 10


def test_check_winner():
    assert check_winner(19, 18, 2000, 1000) == 4000
    assert check_winner(18, 19, 2000, 1000) == 2000
    assert check_winner(21, 21, 2000, 1000) == 3000
    assert check_winner("11/21", "11/21", 2000, 1000) == 3000
    assert check_winner("10/20", 16, 2000, 1000) == 4000
    assert check_winner(16, "7/17", 2000, 1000) == 2000
