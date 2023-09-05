from apps.monitoreo.application.services.congruence_service import CongruenceService
from apps.monitoreo.domain.models.congruence_model import CongruenceModel
class CongruenceController:
    def __init__(self):
        super().__init__()
        self.congruence_service = CongruenceService()

    def resolve_congruence(self, congruence_model: CongruenceModel):
        return self.congruence_service.resolve_congruence(congruence_model)

    def set_test_list(self, congruence_model: CongruenceModel):
        return self.congruence_service.set_test_list(congruence_model)

    def test_congruence(self, congruence_model: CongruenceModel):
        return self.congruence_service.test_congruence(congruence_model)
