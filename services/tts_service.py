import pyttsx3


class TTSService:

    def speak(self, text):

        text = str(text).strip()

        if not text:
            return

        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            170
        )

        engine.setProperty(
            "volume",
            1.0
        )

        engine.say(text)

        engine.runAndWait()

        engine.stop()