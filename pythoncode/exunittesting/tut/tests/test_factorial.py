from program import factorial

def test_factorial():
    assert factorial.fact(1) == 1
    assert factorial.fact(2) == 2
    assert factorial.fact(3) == 6
    assert factorial.fact(4) == 24
