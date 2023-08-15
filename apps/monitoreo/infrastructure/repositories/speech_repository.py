from apps.monitoreo.application.repositories_interfaces.speech_repository_interface import SpeechRepositoryInterface
from apps.monitoreo.domain.models.speech_model import SpeechModel
class SpeechRepository(SpeechRepositoryInterface):
    def __init__(self):
        super().__init__()

    def run_speech(self, speech_model: SpeechModel):
        return speech_model
