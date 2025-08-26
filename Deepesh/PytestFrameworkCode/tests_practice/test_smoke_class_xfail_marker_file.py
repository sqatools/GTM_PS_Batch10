import pytest

class TestBasicCases:

    @pytest.mark.smoke
    def test_addition(self):
        n1 = 40
        n2 = 50
        assert n1+n2 == 90

    @pytest.mark.smoke
    def test_multiplication(self):
        x1 = 4
        x2 = 5
        assert x1*x2 == 20

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.xfail
    def test_subtraction(self):
        x1 = 400
        x2 = 50
        assert x1 - x2 == 350

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_division(self):
        x1 = 40
        x2 = 5
        assert x1//x2 == 9

    @pytest.mark.regression
    def test_greeting(self):
        print("Welcome to Pytest")

    @pytest.mark.regression
    def testWelcomeMsg(self):
        print("Welcome to Pytest class concept")

    @pytest.mark.regression
    def testWelcomeMsg_2(self):
        print("Welcome to Pytest class concept")