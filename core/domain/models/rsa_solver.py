class RsaSolver:

    def __init__(self, array: list[list[float]], p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.array: array
        self.result = []

    def euler(self):
        return (self.p - 1) * (self.q - 1)
    
    def get_d(self, e):
        euler = self.euler()
        for i in range(1, euler):
            if (i * e) % euler == 1:
                return i
    
    def get_e(self):
        for i in range(2, self.euler()):
            if self.euler() % i != 0:
                return i
    