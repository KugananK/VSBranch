from program import vowels

def test_voewls():
    assert vowels.vowels("RYAN") == 1
    assert vowels.vowels("ryan") == 1
    assert vowels.vowels("AEIOU") == 5
    assert vowels.vowels("aeiou") == 5