import datetime
from apps.monitoreo.application.services_interfaces.speak_service_interface import SpeakServiceInterface
from apps.monitoreo.infrastructure.repositories.speak_repository import SpeakRepository
from apps.monitoreo.domain.models.speak_model import SpeakModel
import pyttsx3
from pydub import AudioSegment

from core.util.path.path_helper import PathHelper

class SpeakService(SpeakServiceInterface):
    def __init__(self):
        super().__init__()
        self.speak_repository = SpeakRepository()

    def run_speak(self, speak_model: SpeakModel):
        
        # Inicializa el motor de síntesis de voz
        engine = pyttsx3.init()

        # Configura la tasa de voz y el volumen (estos valores pueden ser ajustados según tus preferencias)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)

        # Aqui tenemos el Datetime en milisegundos formato numerico
        millisecond = datetime.now().timestamp()

        # Guarda el audio generado en un archivo temporal
        engine.save_to_file(speak_model.text, 'temp.mp3')
        engine.runAndWait()  # Espera a que se complete la síntesis de voz

        # Usa pydub para convertir el mp3 a wav (opcional, según tu necesidad)
        path_helper = PathHelper
        root_path = path_helper.get_project_root_path()
        file_path = f"{root_path}/speaks/{speak_model.output_file_name}.wav"

        audio = AudioSegment.from_mp3('temp.mp3')
        audio.export(speak_model.output_file, format="wav")

        return self.speak_repository.run_speak(speak_model)
