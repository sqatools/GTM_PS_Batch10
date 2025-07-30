def test_addition():
    n1 = 40
    n2 = 50
    assert n1+n2 == 90

def test_multiplication():
    x1 = 4
    x2 = 5
    assert x1*x2 == 20

def test_subtraction():
    x1 = 400
    x2 = 50
    assert x1 - x2 == 350


def test_division():
    x1 = 40
    x2 = 5
    assert x1//x2 == 9


def test_greeting():
    print("Welcome to Pytest")