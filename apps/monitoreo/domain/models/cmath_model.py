from core.domain.models.histogram import Histogram


class CmathModel:
    def __init__(self):
        self.list: list[Histogram] = []
        pass

    def to_dict(self):
        return {
            "list": [histogram.to_dict() for histogram in self.list]
        }


