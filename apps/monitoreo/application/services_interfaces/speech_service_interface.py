from abc import ABC, abstractmethod
from apps.monitoreo.domain.models.speech_model import SpeechModel
class SpeechServiceInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def run_speech(self, speech_model: SpeechModel):
        return speech_model
