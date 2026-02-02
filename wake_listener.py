import azure.cognitiveservices.speech as speechsdk


class WakeWordListener:
    def __init__(self, azure_key, azure_region, wake_word="assistant"):
        self.wake_word = wake_word.lower()
        self.speech_config = speechsdk.SpeechConfig(
            subscription=azure_key, region=azure_region)
        self.recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config)

    def wait_for_wake(self):
        print("🎙 Listening for wake word...")

        while True:
            result = self.recognizer.recognize_once()
            if result.text:
                text = result.text.lower()
                print("Heard:", text)

                if self.wake_word in text:
                    print("🔥 Wake word detected!")
                    return
