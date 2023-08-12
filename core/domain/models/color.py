class Color:

    def __init__(self, id=0, intensity=0, expanded_value=0.0, occurrences = 0):
        self.id: int = id
        self.occurrences: int = occurrences
        self.intensity: int = intensity
        self.expanded_value: float = expanded_value

        self.relative_frecuency: float = 0.0
        self.equalized_value: float = 0.0

    def to_dict(self):
        return {
            "intensity": self.intensity,
            "expanded_value": self.expanded_value,
            "occurrences": self.occurrences,
            "relative_frecuency": self.relative_frecuency,
            "equalized_value": self.equalized_value
        }