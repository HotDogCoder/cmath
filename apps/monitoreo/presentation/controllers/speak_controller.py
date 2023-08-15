from apps.monitoreo.application.services.speak_service import SpeakService
from apps.monitoreo.domain.models.speak_model import SpeakModel
class SpeakController:
    def __init__(self):
        super().__init__()
        self.speak_service = SpeakService()

    def run_speak(self, speak_model: SpeakModel):
        return self.speak_service.run_speak(speak_model)
