import pytest


class Test:
    @staticmethod
    @pytest.mark.parametrize("x, y, result", [(1, 1, 1), (2, 2, 4), (10, 0, 0)])
    @pytest.mark.run(order=2)
    def test_multiplication(x, y, result, set_up):
        mul = set_up.multiplication(x, y)
        assert mul == result

    @staticmethod
    @pytest.mark.parametrize("x, y, result", [(1, 1, 0), (2, 1, 1), (10, 5, 5)])
    @pytest.mark.run(order=3)
    def test_subtraction(x, y, result, set_up):
        sub = set_up.subtraction(x, y)
        assert sub == result

    @staticmethod
    @pytest.mark.parametrize("exception, divider", [(ZeroDivisionError, 0), (TypeError, '2')])
    @pytest.mark.run(order=1)
    def test_division_errors(exception, divider, set_up):
        with pytest.raises(exception):
            division = set_up.division(5, divider)
