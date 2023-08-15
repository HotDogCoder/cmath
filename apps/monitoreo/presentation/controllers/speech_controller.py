from apps.monitoreo.application.services.speech_service import SpeechService
from apps.monitoreo.domain.models.speech_model import SpeechModel
class SpeechController:
    def __init__(self):
        super().__init__()
        self.speech_service = SpeechService()

    def run_speech(self, speech_model: SpeechModel):
        return self.speech_service.run_speech(speech_model)
