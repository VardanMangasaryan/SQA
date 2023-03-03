import pytest

from for_pytest.maths import MathMethods

math_obj = MathMethods()


def print_function(text):
    return text


@pytest.mark.parametrize('text', ["Armen", 'Vazgen', "Gagik"])
@pytest.mark.fast
def test_print_function(text):
    assert print_function(text) == text


@pytest.mark.parametrize("x, y, result, mult_result",
                         [(1, 0, 0, 0), (2, 2, 0, 4), (10, 0, 10, 0), (5, 4, 1, 20), (10, 8, 2, 80),
                          (100, 10, 90, 1000)])
def test_math(x, y, result, mult_result):
    assert math_obj.subtraction(x, y) == result
    assert math_obj.multiplication(x, y) == mult_result
