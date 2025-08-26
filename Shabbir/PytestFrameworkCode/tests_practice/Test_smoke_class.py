class TestBasicCases:

    def test_addition(self):
        n1 = 40
        n2 = 50
        assert n1+n2 == 90

    def test_multiplication(self):
        x1 = 4
        x2 = 5
        assert x1*x2 == 20

    def test_subtraction(self):
        x1 = 400
        x2 = 50
        assert x1 - x2 == 350


    def test_division(self):
        x1 = 40
        x2 = 5
        assert x1//x2 == 9


    def test_greeting(self):
        print("Welcome to Pytest")

    def testWelcomeMsg(self):
        print("Welcome to Pytest class concept")

    def testWelcomeMsg_2(self):
        print("Welcome to Pytest class concept")