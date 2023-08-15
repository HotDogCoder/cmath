from abc import ABC, abstractmethod
from apps.monitoreo.domain.models.speak_model import SpeakModel
class SpeakRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def run_speak(self, speak_model: SpeakModel):
        return speak_model
