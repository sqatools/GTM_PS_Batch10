import pytest

class TestBasicCasesxfailMarker:

    @pytest.mark.smoke
    def test_add(self):
        a1 = 10
        a2 = 50
        assert a1+a2 == 60

    @pytest.mark.sanity
    def test_sub(self):
        b1 = 100
        b2 = 20
        assert b1-b2 == 80


    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.xfail
    def test_multiply(self):
        c1 = 2
        c2 = 20
        assert c1*c2 == 40

    @pytest.mark.smoke
    @pytest.mark.xfail
    def test_division(self):
        d1 = 100
        d2 = 2
        assert d1//d2 == 80

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_message1(self):
        print("Hello Everyone!!")

    @pytest.mark.sanity
    @pytest.mark.msg
    def testmessage(self):
        print("def with t!!")

    @pytest.mark.sanity
    def test_message(self):
        print("Starting with T!!")



