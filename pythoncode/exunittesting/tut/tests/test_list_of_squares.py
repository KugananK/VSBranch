from program import list_of_squares

def test_list():
    assert list_of_squares.list_of_squares(1) == {1: 1}
    assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3:9, 4: 16, 5: 25}
