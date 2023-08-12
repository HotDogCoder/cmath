from apps.monitoreo.application.services.cmath_service import CmathService
from apps.monitoreo.domain.models.cmath_model import CmathModel
class CmathController:
    def __init__(self):
        super().__init__()
        self.cmath_service = CmathService()

    def test_cmath(self, cmath_model: CmathModel):
        return self.cmath_service.test_cmath(cmath_model)

    def set_test_list(self, cmath_model: CmathModel):
        return self.cmath_service.set_test_list(cmath_model)
