from abc import ABC, abstractmethod
from apps.monitoreo.domain.models.cmath_model import CmathModel
class CmathRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def test_cmath(self, cmath_model: CmathModel):
        return cmath_model

    @abstractmethod
    def set_test_list(self, cmath_model: CmathModel):
        return cmath_model
