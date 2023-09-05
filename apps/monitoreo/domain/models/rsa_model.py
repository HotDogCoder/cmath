from core.domain.helpers.calculus_helper import CalculusHelper
from core.domain.models.rsa_solver import RsaSolver


class RsaModel:
    def __init__(self):
        self.calculus_helper: CalculusHelper = CalculusHelper()
        self.p: int = 0
        self.q: int = 0
        self.n: int = 0
        self.array: list[list[float]] = []
        self.list: list[RsaSolver] = []
        self.result: list[list[float]] = []
        pass





