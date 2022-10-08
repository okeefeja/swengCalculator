from calc import calculate

def test_calculate():
    assert calculate("0+11") == 11
    assert calculate("11+1-3") == 9
    assert calculate("11*2") == 22
    assert calculate("12435+34569-12345*10+50") == eval("12435+34569-12345*10+50")
