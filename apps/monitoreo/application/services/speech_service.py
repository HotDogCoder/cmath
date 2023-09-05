import datetime
from apps.monitoreo.application.services_interfaces.speech_service_interface import SpeechServiceInterface
from apps.monitoreo.domain.models import speak_model
from apps.monitoreo.infrastructure.repositories.speech_repository import SpeechRepository
from apps.monitoreo.domain.models.speech_model import SpeechModel
import pyttsx3
from pydub import AudioSegment

from core.util.path.path_helper import PathHelper

class SpeechService(SpeechServiceInterface):
    def __init__(self):
        self.speech_repository = SpeechRepository()

    def run_speech(self, speech_model: SpeechModel):

        # Inicializa el motor de síntesis de voz
        engine = pyttsx3.init()

        # Configura la tasa de voz y el volumen (estos valores pueden ser ajustados según tus preferencias)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)

        # Aqui tenemos el Datetime en milisegundos formato numerico
        millisecond = datetime.now().timestamp()

        # Guarda el audio generado en un archivo temporal
        engine.save_to_file(speech_model.text, 'temp.mp3')
        engine.runAndWait()  # Espera a que se complete la síntesis de voz

        # Usa pydub para convertir el mp3 a wav (opcional, según tu necesidad)
        path_helper = PathHelper
        root_path = path_helper.get_project_root_path()
        file_path = f"{root_path}/speaks/{speech_model.output_file_name}.wav"

        audio = AudioSegment.from_mp3('temp.mp3')
        audio.export(file_path, format="wav")



        return self.speech_repository.run_speech(speech_model)
