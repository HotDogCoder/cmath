import pyttsx3
from pydub import AudioSegment

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text, filename="output.mp3"):
        # Save speech to a temporary WAV file
        temp_wav = "temp.wav"
        self.engine.save_to_file(text, temp_wav)
        self.engine.runAndWait()
        
        # Convert the WAV file to MP3 using pydub
        sound = AudioSegment.from_wav(temp_wav)
        sound.export(filename, format="mp3")