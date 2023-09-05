from core.domain.helpers.calculus_helper import CalculusHelper


class CongruenceSolver:

    def __init__(self) -> None:
        # ax = b mod c
        # a = multiplicand of b + c
        self.a_value: float = 0.0
        self.b_value: float = 0.0
        self.c_value: float = 0.0
        self.calculus_helper: CalculusHelper = CalculusHelper()
        pass

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)

    def mcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.mcd(b, a % b)