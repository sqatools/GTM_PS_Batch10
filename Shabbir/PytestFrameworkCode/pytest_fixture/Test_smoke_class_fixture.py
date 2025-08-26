"""
function scope: function level scope fixture will execute along with each function, before and after each test execution
class scope: class level fixture will execute before and after execution of test class.
module scope :  module level fixture will execute on basis on each python file module.
package scope : package level fixture will execute on basis package execution.
session scope : session level fixture will execute along with pytest session
"""
import pytest

@pytest.fixture(scope='function', autouse=True)
def fun_fix():
    """
    we define the fixture function as parameter to specific test function,
    or we can use autouser=True property to apply the execution on each of
    test function automatically.

    :return:
    """
    print("\n-- initiate function fixture ---")
    yield
    print("\n-- end of function fixture ---")


@pytest.fixture(scope='class')
def class_fix():
    print("\n-- initiate class fixture ---")
    yield
    print("\n-- end of class fixture ---")

@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print("\n-- initiate module fixture ---")
    yield
    print("\n-- end of module fixture ---")

@pytest.fixture(scope='package', autouse=True)
def package_fixture():
    print("\n-- initiate package fixture ---")
    yield
    print("\n-- end of package fixture ---")

@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print("\n-- initiate session fixture ---")
    yield
    print("\n-- end of session fixture ---")

@pytest.mark.usefixtures("class_fix")
class TestBasicCases:

    def test_addition(self, fun_fix):
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