import pytest
from src import calculator

def test_divide():
    assert calculator.divide(5,1) ==5