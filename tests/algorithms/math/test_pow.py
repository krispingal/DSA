import cmath
import pytest

from src.dsa.algorithms.math.pow import fast_exponentiation


class TestPow:

    @pytest.mark.parametrize(
        "base, exponent, expected, msg",
        [
            (2.0, 10, 1024.0, "Exponentiation works with positive exponents"),
            (2.0, -2, 0.2500, "Exponentiation works negative numbers"),
            (2.1, 10, 1667.9880978201006, "Exponentiation works large numbers"),
            (2.1, 221, 1.6235442735369674e71, "Exponentiation works large numbers"),
            (2.0, 0, 1.0, "Exponentiation with zero returns 1.0"),
            (
                2.1,
                -213,
                2.3296475481140493e-69,
                "Exponentiation works very small numbers",
            ),
        ],
    )
    def test_pow(self, base, exponent, expected, msg):
        actual = fast_exponentiation(base, exponent)
        assert cmath.isclose(actual, expected, rel_tol=0.02), msg

    @pytest.mark.xfail(raises=ValueError, strict=True)
    def test_pow_invalid_value(self):
        fast_exponentiation(0.0, -1)
