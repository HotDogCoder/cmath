from apps.monitoreo.application.services.rsa_service import RsaService
from apps.monitoreo.domain.models.rsa_model import RsaModel
class RsaController:
    def __init__(self):
        super().__init__()
        self.rsa_service = RsaService()

    def do_rsa(self, rsa_model: RsaModel):
        return self.rsa_service.do_rsa(rsa_model)

    def undo_rsa(self, rsa_model: RsaModel):
        return self.rsa_service.undo_rsa(rsa_model)

    def set_test_list(self, rsa_model: RsaModel):
        return self.rsa_service.set_test_list(rsa_model)

    def test_rsa(self, rsa_model: RsaModel):
        return self.rsa_service.test_rsa(rsa_model)
