from apps.monitoreo.application.services_interfaces.rsa_service_interface import RsaServiceInterface
from apps.monitoreo.infrastructure.repositories.rsa_repository import RsaRepository
from apps.monitoreo.domain.models.rsa_model import RsaModel
class RsaService(RsaServiceInterface):
    def __init__(self):
        super().__init__()
        self.rsa_repository = RsaRepository()

    def do_rsa(self, rsa_model: RsaModel):
        return self.rsa_repository.do_rsa(rsa_model)

    def undo_rsa(self, rsa_model: RsaModel):
        return self.rsa_repository.undo_rsa(rsa_model)

    def set_test_list(self, rsa_model: RsaModel):
        return self.rsa_repository.set_test_list(rsa_model)

    def test_rsa(self, rsa_model: RsaModel):
        return self.rsa_repository.test_rsa(rsa_model)
