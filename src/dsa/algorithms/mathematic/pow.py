"""Implements pow function."""


def fast_exponentiation(base: float, exp: int) -> float:
    """
    Computes the result of raising a base to a power (exponent) using an efficient iterative method.

    This function handles positive, negative, and zero exponents efficiently using the fast
    exponentiation (exponentiation by squaring) technique.

    Args:
        base (float): The base number to be raised to the power.
        exp (int): The exponent to which the base is raised. Can be positive, negative, or zero.

    Returns:
        float: The result of `base` raised to the power `exp`.

    Raises:
        ValueError: If `base` is 0 and `exp` is negative, as the result would be undefined.

    Example:
        >>> result = fast_exponentiation(2, 10)
        >>> print(result)
        1024.0
        >>> result = fast_exponentiation(2, -3)
        >>> print(result)
        0.125
        >>> result = fast_exponentiation(2, 0)
        >>> print(result)
        1.0

    Notes:
        - **Performance**:
            - Time Complexity: O(log n), where `n` is the absolute value of the exponent.
            - Space Complexity: O(1).
        - Handles both positive and negative exponents, including `0` as the exponent.
        - For `base=0` and `exp=0`, the return value is defined as `1.0` (consistent with Python's `math.pow` behavior).

    Warnings:
        - Avoid using `base=0` with a negative exponent, as it raises a `ValueError`.
    """
    if base == 0 and exp < 0:
        raise ValueError(
            "Undefined result: base 0 cannot be raised to a negative exponent."
        )

    if exp < 0:
        base, exp = 1 / base, -exp
    res = 1
    while exp > 0:
        if exp % 2:
            res *= base
        base *= base
        exp //= 2
    return res
