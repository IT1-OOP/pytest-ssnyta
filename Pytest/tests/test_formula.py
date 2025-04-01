import pytest
import math
from . import formula

def test_quadro():
    assert formula.solve_quadratic_formula(1, 2, 1) == (-1.0, -1.0)
