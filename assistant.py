from wake_listener import WakeWordListener
from transcriber import AzureTranscriber
from openai_client import OpenAIClient
from eleven_tts import ElevenLabsTTS
from audio_player import AudioPlayer


class MimirAssistant:
    def __init__(self, azure_key, azure_region, openai_key, eleven_key, voice_id):
        self.listener = WakeWordListener(azure_key, azure_region)
        self.transcriber = AzureTranscriber(azure_key, azure_region)
        self.openai = OpenAIClient(openai_key)
        self.tts = ElevenLabsTTS(eleven_key, voice_id)
        self.player = AudioPlayer()

        self.exit_phrases = [
            "end conversation",
            "stop listening",
            "goodbye",
            "go to sleep",
            "never mind"
        ]

    def run(self):
        print("🤖 Mimir is running...")

        while True:
            # ---- WAIT FOR WAKE WORD ----
            self.listener.wait_for_wake()
            print("🟢 Conversation started")

            while True:
                # ---- LISTEN ----
                text = self.transcriber.transcribe()

                if not text:
                    continue

                lowered = text.lower()

                # ---- EXIT CONVERSATION ----
                if any(p in lowered for p in self.exit_phrases):
                    print("🔴 Conversation ended")
                    break

                # ---- THINK ----
                reply = self.openai.ask(text)

                # ---- SPEAK ----
                audio_file = self.tts.generate(reply)
                self.player.play(audio_file)

                print("🟡 Waiting for next input...")
