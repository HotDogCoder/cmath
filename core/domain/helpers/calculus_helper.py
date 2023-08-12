class CalculusHelper:

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2
        pass

    def to_dict(self):
        return {
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2
        }

    def get_line_pendient(self):
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        return m
    
    def get_line_order(self, target = 1):
        m = self.get_line_pendient()
        if target == 1:
            b = (m * self.x2 - self.x1)*-1
        elif target == 2:
            b = (m * self.y2 - self.y1)*-1
        return b

    def get_y(self, m, b, x):
        # return m * x + b
        return m * x + b
    
    def get_x(self, m, b, y):
        return (y - b) / m
    
    def get_distance(self, x1, y1, x2, y2):
        # aqui se calcula la distancia entre dos puntos
        # se usa ** para elevar a la potencia
        # se ** con 0.5 para sacar la raiz cuadrada
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
