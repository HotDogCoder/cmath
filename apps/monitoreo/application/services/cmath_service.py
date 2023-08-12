from apps.monitoreo.application.services_interfaces.cmath_service_interface import CmathServiceInterface
from apps.monitoreo.infrastructure.repositories.cmath_repository import CmathRepository
from apps.monitoreo.domain.models.cmath_model import CmathModel

class CmathService(CmathServiceInterface):
    def __init__(self):
        super().__init__()
        self.cmath_repository = CmathRepository()

    def test_cmath(self, cmath_model: CmathModel):

        

        return self.cmath_repository.test_cmath(cmath_model)

    def set_test_list(self, cmath_model: CmathModel):
        return self.cmath_repository.set_test_list(cmath_model)
