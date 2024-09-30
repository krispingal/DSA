class Pow:
    def fast_exponentiation(self, base: float, exp: int) -> float:
        if exp < 0:
            base, exp = 1 / base, -exp
        res = 1
        while exp > 0:
            if exp % 2:
                res *= base
            base *= base
            exp //= 2
        return res
