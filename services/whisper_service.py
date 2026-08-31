from groq import Groq

from config import GROQ_API_KEY


class WhisperService:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def transcribe(self, audio_file):

        file_path = "audio/temp_audio.wav"

        with open(file_path, "wb") as f:

            f.write(
                audio_file.getbuffer()
            )

        with open(file_path, "rb") as file:

            transcription = (
                self.client.audio.transcriptions.create(
                    file=file,
                    model="whisper-large-v3-turbo",
                    response_format="text"
                )
            )

        return str(transcription)