from apps.monitoreo.application.repositories_interfaces.speak_repository_interface import SpeakRepositoryInterface
from apps.monitoreo.domain.models.speak_model import SpeakModel
class SpeakRepository(SpeakRepositoryInterface):
    def __init__(self):
        super().__init__()

    def run_speak(self, speak_model: SpeakModel):
        return speak_model
