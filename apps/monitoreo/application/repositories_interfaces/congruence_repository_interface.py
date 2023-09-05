from abc import ABC, abstractmethod
from apps.monitoreo.domain.models.congruence_model import CongruenceModel
class CongruenceRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def resolve_congruence(self, congruence_model: CongruenceModel):
        return congruence_model

    @abstractmethod
    def set_test_list(self, congruence_model: CongruenceModel):
        return congruence_model

    @abstractmethod
    def test_congruence(self, congruence_model: CongruenceModel):
        return congruence_model
