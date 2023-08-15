from apps.monitoreo.application.services_interfaces.speech_service_interface import SpeechServiceInterface
from apps.monitoreo.infrastructure.repositories.speech_repository import SpeechRepository
from apps.monitoreo.domain.models.speech_model import SpeechModel
class SpeechService(SpeechServiceInterface):
    def __init__(self):
        super().__init__()
        self.speech_repository = SpeechRepository()

    def run_speech(self, speech_model: SpeechModel):

        speech_model.text_to_speech.speak(speech_model.input)


        return self.speech_repository.run_speech(speech_model)
