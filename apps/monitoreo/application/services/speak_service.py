from apps.monitoreo.application.services_interfaces.speak_service_interface import SpeakServiceInterface
from apps.monitoreo.infrastructure.repositories.speak_repository import SpeakRepository
from apps.monitoreo.domain.models.speak_model import SpeakModel
class SpeakService(SpeakServiceInterface):
    def __init__(self):
        super().__init__()
        self.speak_repository = SpeakRepository()

    def run_speak(self, speak_model: SpeakModel):
        return self.speak_repository.run_speak(speak_model)
