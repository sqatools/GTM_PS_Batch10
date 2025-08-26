# 31/07/2025 Session

"""
function scope: function level scope fixture will execute along with each function, before and after each test execution
class scope: class level fixture will execute before and after execution of test class.
module scope :  module level fixture will execute on basis on each python file module.
package scope : package level fixture will execute on basis package execution.
session scope : session level fixture will execute along with pytest session
"""

import pytest

@pytest.fixture(scope='function',autouse=True)
def fun_fix():
    """
        we define the fixture function as parameter to specific test function,
        or we can use autouse=True property to apply the execution on each of
        test function automatically.

        :return:
        """
    print("\n-- initiate function fixture ---\n")
    yield
    print("\n-- end of function fixture ---\n")

@pytest.fixture(scope='class')
def class_fix():
    print("\n-- initiate class fixture ---\n")
    yield
    print("\n-- end of class fixture ---\n")

@pytest.fixture(scope='module',autouse=True)
def module_fix():
    print("\n-- initiate module fixture ---\n")
    yield
    print("\n-- end of module fixture ---\n")

@pytest.fixture(scope='package',autouse=True)
def package_fix():
    print("\n-- initiate package fixture ---\n")
    yield
    print("\n-- end of package fixture ---\n")

@pytest.fixture(scope='session',autouse=True)
def session_fix():
    print("\n-- initiate session fixture ---\n")
    yield
    print("\n-- end of session fixture ---\n")

@pytest.mark.usefixtures("class_fix")
class TestBasicCases:
    def test_add(self,fun_fix):
        a1 = 10
        a2 = 50
        assert a1+a2 == 60

    def test_sub(self):
        b1 = 100
        b2 = 20
        assert b1-b2 == 80

    def test_multiply(self):
        c1 = 2
        c2 = 20
        assert c1*c2 == 40

    def test_division(self):
        d1 = 100
        d2 = 2
        assert d1//d2 == 50

    def test_message1(self):
        print("Hello Everyone!!")
