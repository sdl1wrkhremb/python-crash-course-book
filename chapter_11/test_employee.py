import pytest
from employee import Employee


@pytest.fixture
def employee():
    """an employee object that will be availble to all test functions"""
    employee = Employee('bob', 'smith', 50_000)
    return employee


def test_give_default_raise(employee):
    """is a raise added when no raise amount is given"""
    employee.give_raise()
    assert employee.salary == 55_000


def test_give_custom_raise(employee):
    """is a raise added when a custom raise amount is given"""
    employee.give_raise(20000)
    assert employee.salary == 70_000
