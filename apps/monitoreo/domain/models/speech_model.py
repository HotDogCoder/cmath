from core.util.audio.text_to_speech import TextToSpeech


class SpeechModel:
    def __init__(self):
        self.input = None
        self.output = None
        self.text_to_speech = TextToSpeech()
        pass


