from apps.monitoreo.application.services_interfaces.congruence_service_interface import CongruenceServiceInterface
from apps.monitoreo.infrastructure.repositories.congruence_repository import CongruenceRepository
from apps.monitoreo.domain.models.congruence_model import CongruenceModel
class CongruenceService(CongruenceServiceInterface):
    def __init__(self):
        super().__init__()
        self.congruence_repository = CongruenceRepository()

    def resolve_congruence(self, congruence_model: CongruenceModel):
        return self.congruence_repository.resolve_congruence(congruence_model)

    def set_test_list(self, congruence_model: CongruenceModel):
        return self.congruence_repository.set_test_list(congruence_model)

    def test_congruence(self, congruence_model: CongruenceModel):
        return self.congruence_repository.test_congruence(congruence_model)
