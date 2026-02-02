import time
import azure.cognitiveservices.speech as speechsdk


class AzureTranscriber:
    def __init__(self, azure_key, azure_region):
        self.speech_config = speechsdk.SpeechConfig(
            subscription=azure_key, region=azure_region)
        self.audio_config = speechsdk.AudioConfig(use_default_microphone=True)

    def transcribe(self, silence_timeout=2):
        print("🎧 Listening for speech...")
        recognizer = speechsdk.SpeechRecognizer(
            self.speech_config, self.audio_config)

        transcript = []
        last_time = time.time()

        while True:
            result = recognizer.recognize_once()

            if result.text:
                print(">", result.text)
                transcript.append(result.text)
                last_time = time.time()

            if time.time() - last_time > silence_timeout:
                break

        return " ".join(transcript).strip()
