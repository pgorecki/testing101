from example1 import more_negatives


def test_more_neg_than_pos():
    data = [-1, -10, 2]
    assert more_negatives(data) is True


def test_more_pos_than_neg():
    data = [-1, 10, 2]
    assert more_negatives(data) is False


def test_more_equal_neg_pos():
    data = [5, -1, 10, 2]
    assert more_negatives(data) is False


def test_no_numbers():
    data = []
    assert more_negatives(data) is False
