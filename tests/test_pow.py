import cmath
import pytest

from src.dsa.algorithms.pow import Pow

class TestPow:

    @pytest.mark.parametrize("base, exponent, expected, msg", [
        (2.0, 10, 1024.0, "Exponentiation works with positive exponents"),
        (2.0, -2, 0.2500, "Exponentiation works negative numbers"),
        (2.1, 10, 1667.9880978201006, "Exponentiation works large numbers"),
        (2.1, 221, 1.6235442735369674e+71, "Exponentiation works large numbers"),
        (2.1, -213, 2.3296475481140493e-69, "Exponentiation works very small numbers")
    ])
    def test_pow(self, base, exponent, expected, msg):
        pow = Pow()
        actual = pow.fast_exponentiation(base, exponent)
        assert cmath.isclose(actual, expected, rel_tol=0.02), msg