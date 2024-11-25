from employee_code import Employee
import pytest

@pytest.fixture
def sample():
    test = Employee("Vasya", "Poopkin", 5500)
    return test

def test_give_default(sample):
    sample.give_raise()
    assert sample.salary == 10500

def test_give_custom(sample):
    sample.give_raise(4500)
    assert sample.salary == 10000