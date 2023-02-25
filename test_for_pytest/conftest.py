import pytest
from for_pytest.maths import MathMethods


@pytest.fixture(scope='class', autouse=True)
def set_up():
    return MathMethods()
