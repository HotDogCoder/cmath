from apps.monitoreo.application.repositories_interfaces.congruence_repository_interface import CongruenceRepositoryInterface
from apps.monitoreo.domain.models.congruence_model import CongruenceModel
from core.domain.helpers.calculus_helper import CalculusHelper
from core.domain.models.congruence_solver import CongruenceSolver
class CongruenceRepository(CongruenceRepositoryInterface):
    def __init__(self):
        super().__init__()

    def resolve_congruence(self, congruence_model: CongruenceModel):
        return congruence_model

    def set_test_list(self, congruence_model: CongruenceModel):
        congruence_model.list = [
            CongruenceSolver(
                tasks=['equalize', 'expand'],
                id=1,
                calculus_helper=CalculusHelper(x1=3, y1=1, x2=7, y2=7)
            )
        ]

    def test_congruence(self, congruence_model: CongruenceModel):
        return congruence_model
