from abc import ABC, abstractmethod
from apps.monitoreo.domain.models.rsa_model import RsaModel
class RsaRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def do_rsa(self, rsa_model: RsaModel):
        return rsa_model

    @abstractmethod
    def undo_rsa(self, rsa_model: RsaModel):
        return rsa_model

    @abstractmethod
    def set_test_list(self, rsa_model: RsaModel):
        return rsa_model

    @abstractmethod
    def test_rsa(self, rsa_model: RsaModel):
        return rsa_model
